import importlib
import os
import pickle
import random
import shutil
import subprocess
from functools import partial
from itertools import chain
from pathlib import Path

import httpx
from jsonpath_ng import parse

from pytailor.api.dag import TaskType
from pytailor.clients import RestClient, FileClient
from pytailor.clients.handling import handle_file_client_call
from pytailor.exceptions import BackendResponseError, QueryError
from pytailor.models import *
from pytailor.utils import (
    create_rundir,
    extract_real_filenames,
    get_logger,
    list_files,
    as_query,
    format_traceback,
    get_basenames,
    walk_and_apply,
    get_or_create_node_id,
)

CALLABLE_BLACKLIST = [eval, exec, subprocess.call, os.system, os.popen, pickle.load, pickle.loads]


def _resolve_callable(function_name):
    parts = function_name.split(".")

    # class or function
    try:
        func_name = parts[-1]
        module_name = ".".join(parts[:-1])
        function = getattr(importlib.import_module(module_name), func_name)
        return function
    except ModuleNotFoundError:

        # class method
        class_name = parts[-2]
        module_name = ".".join(parts[:-2])
        method_name = parts[-1]
        klass = getattr(importlib.import_module(module_name), class_name)
        function = getattr(klass, method_name)
        return function


MAX_SLEEP_TIME = 60


def _get_sleep_time_seconds(n):
    exp_backoff = 2**n
    jitter = random.random()
    return min(exp_backoff + jitter, MAX_SLEEP_TIME)


class TaskRunner:
    def __init__(self, exec_data: TaskExecutionData, base_dir: Optional[Path]):

        self.__set_exec_data(exec_data)

        # get logger
        self.logger = get_logger("TaskRunner")

        self.base_dir = base_dir or Path.cwd()

        # create a run directory (here or in self.run?)
        friendly_name = f"id{exec_data.task_id}"
        self.run_dir = create_rundir(root_dir=self.base_dir, logger=self.logger, friendly_name=friendly_name)

        self.state = TaskState.RESERVED
        self.local_files = None

    def __set_exec_data(self, exec_data: TaskExecutionData):
        self.__context = exec_data.context.dict() if exec_data.context else None
        self.__task_id = exec_data.task_id
        self.__definition = exec_data.definition
        self.__name = self.__definition["name"] if self.__definition else None
        self.__fileset_id = exec_data.fileset_id
        self.__run_id = exec_data.run_id
        self.__project_id = exec_data.project_id

    def __update_exec_data(self, exec_data: TaskExecutionData):
        self.__context = exec_data.context.dict() if exec_data.context else self.__context
        self.__task_id = exec_data.task_id or self.__task_id
        self.__definition = exec_data.definition or self.__definition
        self.__name = self.__definition["name"] if self.__definition else self.__name
        self.__fileset_id = exec_data.fileset_id or self.__fileset_id
        self.__run_id = exec_data.run_id or self.__run_id
        self.__project_id = exec_data.project_id or self.__project_id

    def run(self):

        self.state = TaskState.RUNNING
        self.logger.info(f"Starting task {self.__task_id}: {self.__name}")

        # step into run dir
        os.chdir(self.run_dir)

        # run job in try/except:
        try:
            self.__execute_task()
        except Exception as e:
            self.__checkin_failed(e)

        # step out of run dir
        os.chdir(self.base_dir)
        self.__cleanup_after_run(self.local_files)
        return True

    def __execute_task(self):
        # call job-type specific code
        task_def = self.__definition
        task_type = TaskType(task_def["type"])
        if task_type is TaskType.PYTHON:
            self.__run_python_task(task_def)
        elif task_type is TaskType.BRANCH:
            self.__run_branch_task()
        elif task_type is TaskType.PIPE:
            self.__run_pipe_task(task_def)

    def __run_python_task(self, task_def):
        # check in state RUNNING, and get exec data
        task_update = TaskUpdate(task_id=self.__task_id, state=self.state, run_dir=str(self.run_dir))
        with RestClient() as client:
            exec_data = client.checkin_task(task_update, wait=True)
        self.__update_exec_data(exec_data)

        self.__maybe_download_files(task_def)
        parsed_args = self.__determine_args(task_def)
        parsed_kwargs = self.__determine_kwargs(task_def)
        function_output = self.__run_function(task_def, parsed_args, parsed_kwargs)
        outputs = self.__extract_output(task_def, function_output)
        if outputs:
            self.__store_output(outputs)
        self.__maybe_upload_files(task_def, function_output)
        self.local_files = self.__maybe_save_local_files(task_def, function_output)
        self.__checkin_completed(self.local_files)

    def __maybe_upload_files(self, task_def, function_output):
        upload = task_def.get("upload")
        # upload must be dict of (tag: val), where val can be:
        #   1:  one or more query expressions(str og list of str) which is applied
        #       to function_output. The query result is searched for file names
        #       pointing to existing files, these files are then uploaded to storage
        #       under the given tag.
        #   2:  one or more glob-style strings (str og list of str) which is applied
        #       in the task working dir. matching files are uploaded under the
        #       given tag.
        if upload:
            files_to_upload = {}
            for tag, v in upload.items():
                if as_query(tag):
                    tag = self.__eval_query(as_query(tag), self.__context)
                if isinstance(v, str):
                    v = [v]
                file_names = []
                for vi in v:
                    if as_query(vi):  # alt 1
                        file_names_i = self.__eval_query(as_query(vi), function_output)
                        file_names_i = extract_real_filenames(file_names_i) or []
                    else:  # alt 2
                        file_names_i = [str(p) for p in list_files(pattern=vi)]
                    file_names.extend(file_names_i)

                if not file_names:
                    raise ValueError(
                        f"For tag '{tag}' the expression(s) {', '.join(v)} " f"did not evaluate to any existing files."
                    )

                files_to_upload[tag] = file_names

            # DO UPLOAD
            fileset_upload = FileSetUpload(task_id=self.__task_id, tags=get_basenames(files_to_upload))
            # get upload links
            with RestClient() as client:
                fileset = client.get_upload_urls(self.__project_id, self.__fileset_id, fileset_upload)
            # do uploads
            with FileClient() as client:
                handle_file_client_call(client.upload_files, files_to_upload, fileset)

    def __maybe_save_local_files(self, task_def, function_output) -> Optional[Dict[str, List[str]]]:
        save_local_files = task_def.get("save_local_files")
        # save_local_files must be dict of (tag: val), where val can be:
        #   1:  one or more query expressions(str og list of str) which is applied
        #       to function_output. The query result is searched for file names
        #       pointing to existing files, these files are then uploaded to storage
        #       under the given tag.
        #   2:  one or more glob-style strings (str og list of str) which is applied
        #       in the task working dir. matching files are uploaded under the
        #       given tag.
        if save_local_files:
            local_files = {}
            for tag, v in save_local_files.items():
                if isinstance(v, str):
                    v = [v]
                file_names = []
                for vi in v:
                    if as_query(vi):  # alt 1
                        file_names_i = self.__eval_query(as_query(vi), function_output)
                        file_names_i = extract_real_filenames(file_names_i) or []
                    else:  # alt 2
                        file_names_i = [str(p) for p in list_files(pattern=vi)]
                    file_names.extend(file_names_i)
                local_files[tag] = [str(Path(fn).absolute()) for fn in file_names]
            return local_files

    def __extract_output(self, task_def, function_output) -> dict:
        outputs = {}
        output_to = task_def.get("output_to")
        if output_to:
            # The entire function_output is put on $.outputs.<output>
            outputs[output_to] = function_output

        output_extraction = task_def.get("output_extraction")
        if output_extraction:
            # For each (tag: query), the query is applied to function_output
            # and the result is put on $.outputs.<tag>
            for k, v in output_extraction.items():
                if isinstance(v, str):
                    q = as_query(v)
                    if q or q == "":
                        val = self.__eval_query(q, function_output)
                    else:
                        raise ValueError("Bad values for *output_extraction* parameter...")
                    outputs[k] = val
                elif isinstance(v, dict):
                    outputs[k] = walk_and_apply(
                        v,
                        val_cond=as_query,
                        val_apply=lambda x: self.__eval_query(as_query(x), function_output),
                    )
        return outputs

    def __store_output(self, outputs):
        task_update = TaskUpdate(run_id=self.__run_id, task_id=self.__task_id, outputs=outputs)
        with RestClient() as client:
            exec_data = client.checkin_task(task_update)
        self.__update_exec_data(exec_data)

    def __run_function(self, task_def, args, kwargs):

        # DONT do this:
        # sys.path.append('.')
        # this has the effect that python modules that have been downloaded are
        # discovered this is potentially risky as users can execute arbitrary code by
        # uploading python modules and calling functions in these modules

        # run callable
        function_name = task_def["function"]
        function = _resolve_callable(function_name)
        if function in CALLABLE_BLACKLIST:
            raise ValueError(f"Function {function_name} is not allowed to be called.")
        self.logger.info(f"Calling: {function_name}")
        function_output = function(*args, **kwargs)
        return function_output

    def __determine_kwargs(self, task_def):
        kwargs = task_def.get("kwargs", {})
        parsed_kwargs = self.__handle_kwargs(kwargs)
        return parsed_kwargs

    def __determine_args(self, task_def):
        args = task_def.get("args", [])
        parsed_args = self.__handle_args(args)
        return parsed_args

    def __maybe_download_files(self, task_def):
        download = task_def.get("download", [])
        download = [download] if isinstance(download, str) else download

        # DO DOWNLOAD
        if download:
            use_storage_dirs = task_def.get("use_storage_dirs", True)
            additional_download_sources = task_def.get("additional_download_sources", [])
            additional_wf_ids = self.__eval_nested(additional_download_sources)
            if isinstance(additional_wf_ids, str):
                additional_wf_ids = [additional_wf_ids]
            elif additional_wf_ids is None:
                additional_wf_ids = []

            for filetag in download:
                if as_query(filetag):
                    filetag = self.__eval_query(as_query(filetag), self.__context)
                try:
                    self.__download_filetag_from_own_fileset(filetag, use_storage_dirs)
                except (BackendResponseError, httpx.HTTPStatusError) as e:
                    if isinstance(e, BackendResponseError) and "Could not retrieve fileset" in str(e):
                        pass
                    elif isinstance(e, httpx.HTTPStatusError) and e.response.status_code == httpx.codes.NOT_FOUND:
                        pass
                    else:
                        raise

                    found = False
                    for wf_id in additional_wf_ids:
                        try:
                            self.__download_filetag_from_other_workflow(wf_id, filetag, use_storage_dirs)
                            found = True
                        except Exception as e:
                            pass
                    if not found:
                        raise

    def __download_filetag_from_own_fileset(self, filetag: str, use_storage_dirs: bool):

        fileset_download = FileSetDownload(task_id=self.__task_id, tags=[filetag])
        with RestClient() as rest_client:
            fileset_getter = partial(
                rest_client.get_download_urls, self.__project_id, self.__fileset_id, fileset_download
            )
            with FileClient() as file_client:
                handle_file_client_call(file_client.download_files, fileset_getter, use_storage_dirs)

    def __download_filetag_from_other_workflow(self, wf_id: str, filetag: str, use_storage_dirs: bool):
        fileset_download = FileSetDownload(tags=[filetag])
        with RestClient() as rest_client:
            fileset_getter = partial(
                rest_client.get_download_urls_from_wf_id, self.__project_id, wf_id, fileset_download
            )
            with FileClient() as file_client:
                handle_file_client_call(file_client.download_files, fileset_getter, use_storage_dirs)

        # add file info to context
        self.__update_context_with_file_info(wf_id, filetag, use_storage_dirs)

    def __update_context_with_file_info(self, wf_id: str, filetag: str, use_storage_dirs: bool):
        # get workflow details
        with RestClient() as client:
            wf = client.get_workflow(self.__project_id, wf_id)

        files_list = wf.files[filetag]
        if not use_storage_dirs:
            files_list = [Path(p).name for p in files_list]
        self.__context["files"][filetag] = files_list

    def __handle_args(self, args):
        q = as_query(args)
        if q:
            parsed_args = self.__eval_query(q, self.__context)
            if not isinstance(parsed_args, list):
                raise TypeError(f"Query expression must evaluate to list. Got " f"{type(parsed_args)}")
        elif not isinstance(args, list):
            raise TypeError(f"*args* must be list or query-expression. Got {type(args)}")
        else:
            parsed_args = self.__eval_nested(args, recurse_into_new_val=True)
        return parsed_args

    def __handle_kwargs(self, kwargs):
        q = as_query(kwargs)
        if q:
            parsed_kwargs = self.__eval_query(q, self.__context)
            if not isinstance(parsed_kwargs, dict):
                raise TypeError(f"Query expression must evaluate to dict. Got " f"{type(parsed_kwargs)}")
        elif not isinstance(kwargs, dict):
            raise TypeError(f"*kwargs* must be dict or query-expression. Got " f"{type(kwargs)}")
        else:
            parsed_kwargs = self.__eval_nested(kwargs, recurse_into_new_val=True)
        return parsed_kwargs

    def __run_branch_task(self):

        task_update = TaskUpdate(
            task_id=self.__task_id,
            perform_branching=True,
            state=self.state,
            run_dir=str(self.run_dir),
        )
        with RestClient() as client:
            exec_data = client.checkin_task(task_update, wait=True)
        self.__update_exec_data(exec_data)
        # don't need to check in completed which is already done backend
        # just update state locally
        self.state = TaskState.COMPLETED

    def __run_pipe_task(self, task_def):
        task_update = TaskUpdate(task_id=self.__task_id, state=self.state, run_dir=str(self.run_dir))
        with RestClient() as client:
            exec_data = client.checkin_task(task_update, wait=True)
        self.__update_exec_data(exec_data)

        pipe_outputs = {}
        pipe_local_files = {}

        for py_task_def in task_def["tasks"]:
            outputs, local_files = self.__run_python_task_from_pipe(py_task_def)
            if outputs:
                self.__context["outputs"].update(outputs)
            if local_files:
                pipe_local_files.update(local_files)

            # we only keep outputs from the last task
            if py_task_def is task_def["tasks"][-1]:
                pipe_outputs = outputs

        self.local_files = pipe_local_files
        self.__store_output(pipe_outputs)
        self.__checkin_completed(pipe_local_files)

    def __run_python_task_from_pipe(self, task_def) -> tuple[dict, dict]:
        self.__maybe_download_files(task_def)
        parsed_args = self.__determine_args(task_def)
        parsed_kwargs = self.__determine_kwargs(task_def)
        function_output = self.__run_function(task_def, parsed_args, parsed_kwargs)
        outputs = self.__extract_output(task_def, function_output)
        self.__maybe_upload_files(task_def, function_output)
        local_files = self.__maybe_save_local_files(task_def, function_output)
        return outputs, local_files

    def __eval_query(self, expression, data):
        vals = [match.value for match in parse(expression).find(data)]
        if not vals:
            raise QueryError(f"Query expression {expression} did not return any data.")
        if len(vals) == 1:
            return vals[0]
        else:
            return vals

    def __eval_nested(self, data, recurse_into_new_val=False):
        val_apply = lambda v: self.__eval_query(as_query(v), self.__context)
        return walk_and_apply(data, val_cond=as_query, val_apply=val_apply, recurse_into_new_val=recurse_into_new_val)

    def __cleanup_after_run(self, local_files: Optional[dict]):
        # delete run dir
        if self.state is TaskState.COMPLETED:  # only remove non-empty run dir if COMPLETED
            if local_files:  # keep local files for later
                run_dir = Path(self.run_dir)
                all_files = [p.absolute() for p in run_dir.rglob("*") if p.is_file()]
                files_to_keep = [Path(p) for p in chain(*local_files.values())]
                for p in set(all_files).difference(files_to_keep):
                    p.unlink()
                # delete now empty dirs
                for p in run_dir.rglob("*"):
                    if p.is_dir():
                        try:
                            p.rmdir()
                        except:
                            pass
            else:
                try:
                    shutil.rmtree(self.run_dir, ignore_errors=True)
                    self.logger.info("Deleted run dir")
                except:
                    self.logger.info("Could not delete run dir", exc_info=1)
        else:  # always remove empty dirs
            try:
                self.run_dir.rmdir()
                self.logger.info("Deleted empty run dir")
            except:  # non-empty dir, leave as is
                pass

    def __checkin_failed(self, e: Exception):
        self.state = TaskState.FAILED

        failure_detail = "".join(format_traceback(e))
        failure_summary = f"Error when executing task {self.__task_id}"
        if hasattr(e, "message"):
            failure_summary: str = e.message

        # check in state FAILED
        task_update = TaskUpdate(
            run_id=self.__run_id,
            task_id=self.__task_id,
            state=self.state,
            failure_detail=failure_detail,
            failure_summary=failure_summary,
        )
        with RestClient() as client:
            exec_data = client.checkin_task(task_update)
        self.__update_exec_data(exec_data)

        self.logger.error(f"Task {self.__task_id} FAILED", exc_info=True)

    def __checkin_completed(self, local_files: Optional[dict]):
        self.state = TaskState.COMPLETED

        # check in state COMPLETED
        task_update = TaskUpdate(
            run_id=self.__run_id,
            task_id=self.__task_id,
            state=self.state,
            local_node_id=get_or_create_node_id(),
            local_files=local_files,
        )
        with RestClient() as client:
            exec_data = client.checkin_task(task_update)
        self.__update_exec_data(exec_data)

        self.logger.info(f"Task {self.__task_id} COMPLETED successfully")


def run_task(checkout: TaskExecutionData, base_dir: Optional[Path] = None):
    runner = TaskRunner(checkout, base_dir)
    return runner.run()
