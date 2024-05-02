import sys
from subprocess import check_output
from typing import Any, Dict, cast

import pytest
from databricks.sdk.service.compute import Library
from databricks.sdk.service.jobs import BaseJob, JobSettings, Task

from databricks_jobs.config import get_pyproject_arguments
from databricks_jobs.update_libraries import (
    _get_requirement_specifier_index_url,
    update_jobs_libraries,
)
from databricks_jobs.utilities import list_jobs

_pyproject_arguments: Dict[str, Any] = get_pyproject_arguments()
TOKEN_CERBERUS_PATH: str = _pyproject_arguments["token_cerberus_path"]
REQUIREMENTS: str = _pyproject_arguments["requirements"]


def test_get_requirement_specifier_index_url(job_name: str) -> None:
    assert job_name
    assert _get_requirement_specifier_index_url(
        "--index-url https://pypi.org/simple"
    ) == ("", "https://pypi.org/simple")
    assert _get_requirement_specifier_index_url(
        "--extra-index-url https://pypi.org/simple"
    ) == ("", "https://pypi.org/simple")
    assert _get_requirement_specifier_index_url(
        "sqlalchemy --extra-index-url https://pypi.org/simple"
    ) == ("sqlalchemy", "https://pypi.org/simple")
    assert _get_requirement_specifier_index_url(
        "--extra-index-url https://pypi.org/simple sqlalchemy"
    ) == ("sqlalchemy", "https://pypi.org/simple")


def validate_requirements(job_name: str) -> None:
    """
    Verify that all job task library requirements are found in our
    requirements file
    """
    job: BaseJob = list_jobs(names=(job_name,))[0]
    with open(REQUIREMENTS, "r") as requirements_io:
        requirements: str = requirements_io.read()
        task: Task
        for task in cast(JobSettings, job.settings).tasks or ():
            library: Library
            for library in task.libraries or ():
                if library.pypi:
                    assert library.pypi.package in requirements


def test_update_jobs_libraries_cli(job_name: str) -> None:
    assert job_name
    # Implicit arguments (from pyproject.toml)
    check_output(
        (
            sys.executable,
            "-m",
            "databricks_jobs",
            "update-libraries",
            job_name,
        )
    )
    # Explicit arguments
    check_output(
        (
            sys.executable,
            "-m",
            "databricks_jobs",
            "update-libraries",
            "-tcp",
            TOKEN_CERBERUS_PATH,
            "-r",
            REQUIREMENTS,
            job_name,
        )
    )
    validate_requirements(job_name)


def test_update_jobs_libraries(job_name: str) -> None:
    assert job_name
    update_jobs_libraries(
        job_names=(job_name,),
    )
    validate_requirements(job_name)


if __name__ == "__main__":
    pytest.main()
