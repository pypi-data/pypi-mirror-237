# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from __future__ import annotations

from abc import ABC
from pathlib import Path
from typing import Union

from airflow.models import Variable, DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.context import Context
from docker.types import Mount
import docker


class NotebookExtensionError(Exception):
    pass


class ReservedParameterError(Exception):
    pass


class RelativePathError(Exception):
    pass


def is_running_on_docker() -> bool:
    """Checks for "/.dockerenv as a test"""
    return Path("/.dockerenv").exists()


class PapermillOperator(DockerOperator):
    CONTAINER_NOTEBOOK_DIR = Path("/opt/airflow/notebooks")
    CONTAINER_NOTEBOOK_OUT_DIR = Path("/opt/airflow/notebooks_out")
    template_fields = (
        *DockerOperator.template_fields,
        "notebook_name",
        "host_notebook_dir",
        "mounts",
        "nb_params",
        "image",
        "host_notebook_out_base_dir",
        "host_notebook_out_taskrun_dir",
        "host_notebook_out_dir",
        "host_notebook_out_path",
        "container_notebook_out_path",
        "container_notebook_out_name",
        "notebook_uid",
        "notebook_gid",
        "user",
    )

    def __init__(
        self,
        *,
        notebook_name: str,
        host_notebook_dir: str,
        host_notebook_out_dir: str,
        nb_params=None,
        image=None,
        mounts=None,
        environment=None,
        **kwargs,
    ):
        if Path(notebook_name).suffix not in [".json", ".ipynb"]:
            raise NotebookExtensionError("Notebooks must have ipynb or json extension")
        if nb_params is None:
            nb_params = {}
        if mounts is None:
            mounts = []
        if environment is None:
            environment = {}
        self.nb_params = nb_params
        self.log.info(f"Creating docker task to run for {notebook_name}")
        self.notebook_uid = Variable.get("NOTEBOOK_UID")
        self.notebook_gid = Variable.get("NOTEBOOK_GID")
        self._user_string = f"{self.notebook_uid}:{self.notebook_gid}"
        self.notebook_name = notebook_name

        self.host_notebook_dir = host_notebook_dir
        self.host_notebook_out_base_dir = host_notebook_out_dir
        self.host_notebook_out_taskrun_dir = (
            "{{ds}}/{{dag.dag_id}}__{{task_instance.task_id}}__{{run_id}}"
        )
        self.host_notebook_out_dir = (
            f"{self.host_notebook_out_base_dir}/{self.host_notebook_out_taskrun_dir}"
        )
        self.container_notebook_out_name = (
            "{{dag.dag_id}}__{{task_instance.task_id}}__{{run_id}}__" f"{notebook_name}"
        )
        self.host_notebook_out_path = (
            f"{self.host_notebook_out_dir}/{self.container_notebook_out_name}"
        )
        self.container_notebook_path = f"{self.CONTAINER_NOTEBOOK_DIR}/{notebook_name}"
        self.container_notebook_out_path = (
            f"{self.CONTAINER_NOTEBOOK_OUT_DIR}/{self.container_notebook_out_name}"
        )

        mounts += [
            Mount(
                source=str(self.host_notebook_dir),
                target=str(self.CONTAINER_NOTEBOOK_DIR),
                type="bind",
                read_only=True,
            ),
            Mount(
                source=str(self.host_notebook_out_dir),
                target=str(self.CONTAINER_NOTEBOOK_OUT_DIR),
                type="bind",
            ),
        ]

        mount_string = "\n".join(f"{m['Source']} to {m['Target']}" for m in mounts)
        self.log.info(f"Mounts:\n {mount_string}")

        param_string = " ".join(
            f"-p {key} {value}" for (key, value) in self.nb_params.items()
        )
        self.log.info("Param string")
        self.log.info(param_string)
        environment["PYTHONPATH"] = f"{str(self.CONTAINER_NOTEBOOK_DIR)}:${{PYTHONPATH}}"
        command = f"papermill {param_string} {self.container_notebook_path} {self.container_notebook_out_path}"

        super().__init__(
            command=command,
            user=self._user_string,
            auto_remove="force",
            image=image,
            mounts=mounts,
            environment=environment,
            **kwargs,
        )

    def execute(self, context: Context):
        self.create_path_on_host(
            self.host_notebook_out_base_dir, self.host_notebook_out_taskrun_dir
        )
        super().execute(context)

    def create_path_on_host(
        self, host_root: Union[Path, str], relative_path: Union[Path, str]
    ):
        self.log.info(f"Attempting to create {relative_path} at {host_root}")
        host_root = Path(host_root)
        relative_path = Path(relative_path)
        if relative_path.is_absolute():
            raise RelativePathError("Path to be created on host cannot be absolute")
        if not is_running_on_docker():
            self.log.info(
                f"Operator running on host, creating {host_root}/{relative_path}"
            )
            (host_root / relative_path).mkdir(exist_ok=True, parents=True)
        else:
            client = docker.DockerClient()
            self.log.info(
                f"Spawning busybox container to create {relative_path} in {host_root}"
                f" using uid {self.notebook_uid} gid {self.notebook_gid}"
            )
            client.containers.run(
                "busybox",
                f"mkdir -p /opt/{relative_path}",
                volumes=[f"{host_root}:/opt"],
                user=self._user_string,
                remove=True,
            )


class FlowpyterOperator(PapermillOperator):
    """
    An operator that runs a parameterised Flowpyter notebook with a shared data area

    Parameters
    ----------
    notebook_name : str
        The name of the notebook to execute (including extension)
    host_notebook_dir
        Folder on the host containing the notebooks to be executed. Mounted read-only.
    host_notebook_out_dir
        Folder on the host that will contain the rendered and executed notebooks
    host_data_dir
        Folder on the host for intermediate data artefacts to be passed between
        tasks in the DAG - see notes
    host_static_dir
        Folder on the host containing static assets. Mounted read-only.
    notebook_params : dict, optional
        Parameters for Papermill to inject into the notebook.
    image : str, default "flowminder/flowpyterlab:api-analyst-latest"
        The Docker image to run the notebook on
    network_mode : str, optional
        The docker compose network mode; see docs for corresponding
        parameter in https://airflow.apache.org/docs/apache-airflow-providers-docker/stable/_api/airflow/providers/docker/operators/docker/index.html
    environment : dict, optional, default FlowpyterOperator.flowapi_env
        Environment variables to be injected into the running Docker environment.


    Notes
    -----

    - Every notebook has a ``data_dir`` variable injected by default - this is a shared folder that can be used to
      pass artefacts between notebooks and other tasks within a dagrun. The following jinja string should give the
      path to the shared data folder;

      ``{{ var.value.host_data_dir }}/{{ ds }}/{{ dag.id }}__{{ run_id }}``
    - The completed notebooks are saved in task-individual folders within ``host_notebook_out_dir``
    - The notebook_params keys and values can also use jinja templating, but this has not been tested yet

    The Airflow variables needed for this operator to run

    host_dag_path
        The path to the dag folder - this is needed to resolve some paths between the host, the scheduler and the
        notebook container
    flowapi_token (optional)
        A token to be passed into the notebooks for
    notebook_uid, notebook_gid
        The uid and gid to run the notebook container as

    Examples
    --------
    This example demonstrates using the data_dir injected variable to write an artefact to the shared area
    in one notebook, and read and print its contents in the other:

    >>> # glue_nb.ipynb
    ... data_dir = "unset"
    ... artifact_out = "unset"
    ... from pathlib import Path
    ... ( Path(data_dir) / artifact_out).write_text("DEADBEEF")
    ...
    ... # read_nb.ipynb
    ... data_dir = "unset"
    ... artifact_in = "unset"
    ... from pathlib import Path
    ... print(( Path(data_dir) / artifact_in).read_text())
    ...
    ... first_nb = FlowpyterOperator(
    ...    task_id="first_task",
    ...    notebook_name="glue_nb.ipynb",
    ...    notebook_params={"artifact_out": "test_artifact.txt"},
    ... )
    ... second_nb = FlowpyterOperator(
    ...    task_id="second_task",
    ...    notebook_name="read_nb.ipynb",
    ...    notebook_params={"artifact_in": "test_artifact.txt"},
    ... )
    ... first_nb >> second_nb
    """

    CONTAINER_STATIC_DIR = Path("/opt/airflow/static")
    CONTAINER_DATA_DIR = Path("/opt/airflow/data")
    RESERVED_PARAMS = ["data_dir", "static_dir"]
    template_fields = [
        *PapermillOperator.template_fields,
        "host_data_root",
        "host_run_data_dir",
        "host_static_dir",
        "mounts",
        "nb_params",
    ]

    # Note - I want this to be something that can be used as a convenience function
    # ex `foo = FlowpyterOperator(...., environment = FlowpyterOperator.flowapi_env)
    # Need to test it out.
    flowapi_env = {
        "FLOWAPI_TOKEN": Variable.get(
            "flowapi_token", "PLEASE SET AIRFLOW_VAR_FLOWAPI_TOKEN IN AIRFLOW HOST"
        ),
        "FLOWAPI_URL": "http://localhost:9090",
    }

    def _check_flowpyter_reserved_keys(self, nb_params):
        if any(r_key in nb_params.keys() for r_key in self.RESERVED_PARAMS):
            raise ReservedParameterError(
                f"{self.RESERVED_PARAMS} are reserved for use by FlowpyterOperator"
            )

    def __init__(
        self,
        *,
        host_data_dir: str,
        host_static_dir: str,
        image: str = "flowminder/flowpyterlab:api-analyst-latest",
        network_mode: str = None,
        environment: dict = None,
        mounts=None,
        nb_params=None,
        **kwargs,
    ) -> None:
        if environment is None:
            environment = self.flowapi_env
        if mounts is None:
            mounts = []
        if nb_params is None:
            nb_params = {}
        self._check_flowpyter_reserved_keys(nb_params)
        self.host_data_root = host_data_dir
        self.host_run_data_dir = "{{ds}}/{{dag.dag_id}}__{{run_id}}"
        self.host_data_dir = f"{self.host_data_root}/{self.host_run_data_dir}"

        self.host_static_dir = host_static_dir
        mounts += [
            Mount(
                source=str(self.host_static_dir),
                target=str(self.CONTAINER_STATIC_DIR),
                type="bind",
                read_only=True,
            ),
            Mount(
                source=str(self.host_data_dir),
                target=str(self.CONTAINER_DATA_DIR),
                type="bind",
            ),
        ]

        context_params = {
            "data_dir": self.CONTAINER_DATA_DIR,
            "static_dir": self.CONTAINER_STATIC_DIR,
        }
        nb_params.update(context_params)

        super().__init__(
            image=image,
            mounts=mounts,
            mount_tmp_dir=False,
            environment=environment,
            network_mode=network_mode,
            nb_params=nb_params,
            **kwargs,
        )

    def execute(self, context):
        self.create_path_on_host(self.host_data_root, self.host_run_data_dir)
        super().execute(context)


class TemplateOperator(PapermillOperator):
    RESERVED_PARAMS = ["data_dir", "template_dir"]
    CONTAINER_TEMPLATE_DIR = "/opt/airflow/templates"
    CONTAINER_DATA_DIR = "/opt/airflow/data"

    template_fields = [
        *PapermillOperator.template_fields,
        "host_data_root",
        "host_run_data_dir",
        "host_data_dir",
        "host_template_dir",
        "mounts",
        "nb_params",
    ]

    def __init__(
        self,
        *,
        host_template_dir,
        host_data_dir,
        image: str = "flowminder/flowpyterlab:api-analyst-latest",
        mounts=None,
        dag=None,
        nb_params=None,
        **kwargs,
    ):
        if mounts is None:
            mounts = []
        if nb_params is None:
            nb_params = {}
        self._check_template_reserved_keys(nb_params)
        self.host_data_root = host_data_dir
        self.host_run_data_dir = "{{ds}}/{{dag.dag_id}}__{{run_id}}"
        self.host_data_dir = f"{self.host_data_root}/{self.host_run_data_dir}"
        self.host_template_dir = host_template_dir
        mounts += (
            Mount(
                source=str(self.host_template_dir),
                target=str(self.CONTAINER_TEMPLATE_DIR),
                type="bind",
                read_only=True,
            ),
            Mount(
                source=str(self.host_data_dir),
                target=str(self.CONTAINER_DATA_DIR),
                type="bind",
            ),
        )
        context_params = {
            "data_dir": self.CONTAINER_DATA_DIR,
            "template_dir": self.CONTAINER_TEMPLATE_DIR,
        }
        nb_params.update(context_params)
        super().__init__(
            image=image, mounts=mounts, dag=dag, nb_params=nb_params, **kwargs
        )

    def _check_template_reserved_keys(self, nb_params):
        if any(r_key in nb_params.keys() for r_key in self.RESERVED_PARAMS):
            raise ReservedParameterError(
                f"{self.RESERVED_PARAMS} are reserved for use by TemplateOperator"
            )

    def execute(self, context):
        self.create_path_on_host(self.host_data_root, self.host_run_data_dir)
        super().execute(context)
