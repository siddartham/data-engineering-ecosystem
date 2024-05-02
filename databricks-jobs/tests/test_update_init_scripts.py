import sys
from subprocess import check_output
from typing import Any, Dict, Tuple, cast

import pytest
from databricks.sdk.service.compute import (
    ClusterSpec,
    InitScriptInfo,
    WorkspaceStorageInfo,
)
from databricks.sdk.service.jobs import BaseJob, JobSettings

from databricks_jobs.config import get_pyproject_arguments
from databricks_jobs.update_init_scripts import (
    _get_job_task_cluster_spec,
    update_jobs_init_scripts,
)
from databricks_jobs.upload import upload
from databricks_jobs.utilities import list_jobs

_pyproject_arguments: Dict[str, Any] = get_pyproject_arguments()
TOKEN_CERBERUS_PATH: str = _pyproject_arguments["token_cerberus_path"]
REQUIREMENTS: str = _pyproject_arguments["requirements"]
INIT_SCRIPTS: Tuple[str, ...] = tuple(
    sorted(_pyproject_arguments["init_scripts"])
)
FILES: Dict[str, str] = _pyproject_arguments["files"]


def validate(job_name: str) -> None:
    """
    Verify that the init scripts were applied as expected
    """
    job: BaseJob = list_jobs(names=(job_name,))[0]
    for task in cast(JobSettings, job.settings).tasks or ():
        cluster_spec: ClusterSpec = _get_job_task_cluster_spec(job, task)
        init_script: InitScriptInfo
        assert (
            tuple(
                sorted(
                    cast(
                        WorkspaceStorageInfo, init_script.workspace
                    ).destination
                    or ""
                    for init_script in (cluster_spec.init_scripts or ())
                )
            )
            == INIT_SCRIPTS
        ), f"Expected {INIT_SCRIPTS}, got {cluster_spec.init_scripts}"


def cleanup(job_name: str) -> None:
    """
    Delete test file from workspace
    """
    update_jobs_init_scripts(job_names=(job_name,), init_scripts=())


def test_update_jobs_init_scripts_cli(job_name: str) -> None:
    assert job_name
    upload()
    # Implicit arguments (from pyproject.toml)
    check_output(
        (
            sys.executable,
            "-m",
            "databricks_jobs",
            "update-init-scripts",
            job_name,
        )
    )
    validate(job_name)
    cleanup(job_name)
    upload()
    # Explicit arguments
    command: Tuple[str, ...] = (
        sys.executable,
        "-m",
        "databricks_jobs",
        "update-init-scripts",
        "-tcp",
        TOKEN_CERBERUS_PATH,
    )
    init_script: str
    for init_script in INIT_SCRIPTS:
        command += ("-is", init_script)
    command += (job_name,)
    check_output(command)
    validate(job_name)


def test_update_jobs_init_scripts(job_name: str) -> None:
    assert job_name
    upload()
    update_jobs_init_scripts((job_name,))
    validate(job_name)
    cleanup(job_name)


if __name__ == "__main__":
    pytest.main()
