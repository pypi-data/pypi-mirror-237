from __future__ import annotations

import os
from typing import Optional, List

from .schema import InputsSchema, FilesSchema

from .schema.description import Description
from pytailor.clients import RestClient
from pytailor.api.base import APIBase
from pytailor.exceptions import BackendResourceError
from pytailor.models import WorkflowDefinition as WorkflowDefinitionModel
from pytailor.models import WorkflowDefinitionCreate
from pytailor.utils import dict_keys_str_to_int, dict_keys_int_to_str
from .account import Account
from .dag import DAG
from .project import Project
from .workflow import Workflow


class WorkflowDefinition(APIBase):
    """
    Create a new workflow definition.
    Workflow Definitions are parameterized and reusable blueprints for computing workflows.

    **Parameters:**

    - **name** str, optional
        Provide a name for this workflow definition.
    - **dag** : DAG
        Provide a dag object for this workflow definition.
    - **inputs_schema** dict, optional
        JSON-schema for rendering of inputs in the react web app and validating the structure and data typing of the
        input parameters (dict)
    - **outputs_schema** dict, optional
        JSON-schema for validating the structure and data typing of the
        output parameters (dict)
    - **files_schema** dict, optional
        JSON-file for rendering of file upload tab in the react web app and
        validating file extensions etc.
    """

    def __init__(
        self,
        name: str,
        description: str,
        dag: DAG,
        inputs_schema: Optional[dict] = None,
        outputs_schema: Optional[dict] = None,
        files_schema: Optional[dict] = None,
    ):

        self.__name = name
        self.__description = description
        self.__dag = dag
        self.__inputs_schema = inputs_schema
        self.__outputs_schema = outputs_schema
        self.__files_schema = files_schema
        self.__id = None

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def dag(self):
        return self.__dag

    @property
    def inputs_schema(self):
        return self.__inputs_schema

    @property
    def outputs_schema(self):
        return self.__outputs_schema

    @property
    def files_schema(self):
        return self.__files_schema

    @property
    def id(self):
        return self.__id

    def add_to_account(self, account: Account):
        """
        Add workflow definition to account.

        **Parameters:**

        - **account** (Account):
            The account to add the workflow definition to.
        """

        # check not existing
        if self.__id is not None:
            raise BackendResourceError(
                "Cannot add workflow definition to account. The " "workflow definition already exist backend."
            )

        # make request model
        wf_def_create = WorkflowDefinitionCreate(
            name=self.name,
            description=self.description,
            dag=dict_keys_int_to_str(self.dag.to_dict()),
            inputs_schema=self.inputs_schema,
            outputs_schema=self.outputs_schema,
            files_schema=self.files_schema,
            # TODO: requirements=dag.get_all_requirements()
        )

        # make rest call
        with RestClient() as client:
            wf_def_model = client.new_workflow_definition(account.id, wf_def_create)

        # update self
        self.__update_from_backend(wf_def_model)

    @classmethod
    def from_project_and_id(cls, project: Project, wf_def_id: str) -> WorkflowDefinition:
        """
        Retrieve a single workflow definition from a project.

        **Parameters:**

        - **project** (Project):
            The project to retrieve the workflow definition from.
        - **wf_def_id** (str):
            The id of the workflow definition to retrieve.
        """
        # get workflow definition model
        with RestClient() as client:
            wf_def_model = client.get_workflow_definition_project(project.id, wf_def_id)
        wf_def = cls.__from_model(wf_def_model)
        return wf_def

    @classmethod
    def __from_model(cls, wf_def_model: WorkflowDefinitionModel):
        wf_def = WorkflowDefinition(
            name=wf_def_model.name,
            description=wf_def_model.description,
            dag=dict_keys_int_to_str(DAG.from_dict(wf_def_model.dag)),
            inputs_schema=wf_def_model.inputs_schema,
            outputs_schema=wf_def_model.outputs_schema,
            files_schema=wf_def_model.files_schema,
        )
        wf_def.__update_from_backend(wf_def_model)

        return wf_def

    @classmethod
    def from_workflow(cls, wf: Workflow, wf_def_name: str, wf_def_description: str):
        """
        Create a workflow definition from an existing workflow.

        **Parameters:**

        - **wf** (Workflow):
            The workflow to create the workflow definition from.
        - **wf_def_name** (str):
            The name of the workflow definition.
        - **wf_def_description** (str):
            The description of the workflow definition.
        """
        assert wf.id, "the workflow must be an existing run to access fileset and generate definition"
        description = Description.from_dag(wf.dag, wf_def_name=wf_def_name, wf_def_description=wf_def_description)
        inputs_schema = InputsSchema(inputs=wf.inputs)
        inputs_schema.add_defaults(wf.inputs)
        files_schema = FilesSchema.from_fileset_and_dag(fileset=wf.fileset, dag=wf.dag)

        return cls(
            name=description.name,
            description=description.to_string(),
            dag=wf.dag,
            inputs_schema=inputs_schema.to_dict(),
            outputs_schema=None,
            files_schema=files_schema.to_dict(),
        )

    def __update_from_backend(self, wf_def_model: WorkflowDefinitionModel):
        self.__id = wf_def_model.id
