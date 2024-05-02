import sys
from subprocess import check_output
from typing import Any, Dict

import pytest
from databricks.sdk import WorkspaceClient

from databricks_jobs.client import get_workspace_client
from databricks_jobs.config import get_pyproject_arguments
from databricks_jobs.upload import upload

DIRECTORY: str = "/Workspace/Shared/databricks-jobs-test"

_pyproject_arguments: Dict[str, Any] = get_pyproject_arguments()
TOKEN_CERBERUS_PATH: str = _pyproject_arguments["token_cerberus_path"]
REQUIREMENTS: str = _pyproject_arguments["requirements"]
WORKSPACE_REQUIREMENTS_TEMPLATE: str = (
    "/Workspace/Shared/databricks-jobs-test/requirements-{}.txt"
)


def validate(job_name: str) -> None:
    """
    Verify that uploaded file matches the local file
    """
    client: WorkspaceClient = get_workspace_client()
    with client.workspace.download(
        WORKSPACE_REQUIREMENTS_TEMPLATE.format(job_name)
    ) as downloaded_io:
        with open(REQUIREMENTS, "rb") as requirements_io:
            assert downloaded_io.read() == requirements_io.read()


def cleanup(job_name: str) -> None:
    """
    Delete test file from workspace
    """
    client: WorkspaceClient = get_workspace_client()
    client.workspace.delete(WORKSPACE_REQUIREMENTS_TEMPLATE.format(job_name))


def test_upload_cli(job_name: str) -> None:
    assert job_name
    # Implicit arguments (from pyproject.toml)
    check_output(
        (
            sys.executable,
            "-m",
            "databricks_jobs",
            "upload",
            "-f",
            REQUIREMENTS,
            WORKSPACE_REQUIREMENTS_TEMPLATE.format(job_name),
        )
    )
    validate(job_name)
    cleanup(job_name)
    # Explicit arguments
    check_output(
        (
            sys.executable,
            "-m",
            "databricks_jobs",
            "upload",
            "-tcp",
            TOKEN_CERBERUS_PATH,
            "-f",
            REQUIREMENTS,
            WORKSPACE_REQUIREMENTS_TEMPLATE.format(job_name),
        )
    )
    validate(job_name)
    cleanup(job_name)


def test_upload(job_name: str) -> None:
    assert job_name
    upload({REQUIREMENTS: WORKSPACE_REQUIREMENTS_TEMPLATE.format(job_name)})
    validate(job_name)
    cleanup(job_name)


if __name__ == "__main__":
    pytest.main()
