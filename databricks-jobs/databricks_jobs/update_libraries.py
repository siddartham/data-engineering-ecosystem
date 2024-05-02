import argparse
import re
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple, Union, cast

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.compute import Library, PythonPyPiLibrary
from databricks.sdk.service.jobs import BaseJob, JobSettings, Task

from ._utilities import apply_defaults, as_list
from .client import get_workspace_client
from .config import DEFAULT_HOST, get_pyproject_arguments
from .utilities import list_jobs

_INDEX_URL_PATTERN: re.Pattern = re.compile(
    r"--(?:extra-)?index-url\s+(\S+)",
    re.IGNORECASE,
)


def _get_requirement_specifier_index_url(
    requirement_specifier: str,
) -> Tuple[str, str]:
    """
    Parse a requirement file line to separate the requirement specifier from
    from the index URL (if present).
    """
    matched: Optional[re.Match[str]] = _INDEX_URL_PATTERN.search(
        requirement_specifier
    )
    if matched:
        return (
            (
                f"{requirement_specifier[:matched.start()]}"
                f"{requirement_specifier[matched.end():]}"
            ).strip(),
            matched.group(1),
        )
    return requirement_specifier, ""


@as_list
def _get_requirements_libraries(
    requirements: Union[str, Path],
) -> Iterable[Library]:
    with open(requirements) as requirements_io:
        index_url: str = ""
        _index_url: str = ""
        requirement_specifier: str
        for requirement_specifier in (
            requirements_io.read().strip().split("\n")
        ):
            if requirement_specifier.lstrip().startswith("#"):
                continue
            requirement_specifier, _index_url = (
                _get_requirement_specifier_index_url(requirement_specifier)
            )
            if _index_url:
                index_url = _index_url
            if requirement_specifier:
                yield Library(
                    pypi=PythonPyPiLibrary(
                        package=requirement_specifier,
                        repo=index_url,
                    )
                )


@apply_defaults(**get_pyproject_arguments())
def update_jobs_libraries(
    job_names: Sequence[str] = (),
    requirements: Union[str, Path] = "",
    task_keys: Tuple[str, ...] = (),
    host: str = DEFAULT_HOST,
    token: str = "",
    token_cerberus_path: str = "",
) -> None:
    """
    This function updates PYPI libraries for one or more databricks jobs based
    on a provided requirements file.

    Parameters:

    - job_names ([str]|str): The name of the job (or jobs) to update.
    - requirements (str|Path): The path to a requirements file.
    - host (str): The databricks API host.
    - task_keys ((str,)) = (): If provided only tasks with the specified
      keys will be updated.
    - token (str): An authentication token.
    - token_cerberus_path (str): A Cerberus secure drop box path from
      which an authentication token can be retrieved.
    """
    if isinstance(job_names, str):
        job_names = (job_names,)
    jobs: Tuple[BaseJob, ...] = list_jobs(
        names=job_names,
        host=host,
        token=token,
        token_cerberus_path=token_cerberus_path,
    )
    if not jobs:
        raise ValueError(f"No jobs with the names f{job_names} were found.")
    requirement_libraries: List[Library] = _get_requirements_libraries(
        requirements
    )
    client: WorkspaceClient = get_workspace_client(
        **({"host": host} if host else {}),
        **({"token": token} if token else {}),
        **(
            {"token_cerberus_path": token_cerberus_path}
            if token_cerberus_path
            else {}
        ),
    )
    job: BaseJob
    for job in jobs:
        tasks: Optional[List[Task]] = cast(JobSettings, job.settings).tasks
        if not tasks:
            continue
        for task in tasks:
            if (not task_keys) or (task.task_key in task_keys):
                # Filter out pre-existing PYPI libraries, then
                # append the requirement file libraries to the list of
                # libraries which are not PYPI libraries
                task.libraries = (
                    list(
                        filter(
                            lambda library: library.pypi is None,
                            task.libraries or (),
                        )
                    )
                    + requirement_libraries
                )
        # Update the job with our modified settings
        client.jobs.update(
            job_id=cast(int, job.job_id),
            new_settings=cast(JobSettings, job.settings),
        )


def main() -> None:
    """
    This function is the entry point for using this script as a CLI.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="databricks-jobs update-libraries",
        description=(
            "This command updates PYPI libraries for one or more "
            "databricks job(s) based on the provided requirements file"
        ),
    )
    parser.add_argument(
        "-r",
        "--requirements",
        type=str,
        default="",
        help="The path to a requirements file.",
    )
    parser.add_argument(
        "--host",
        type=str,
        default="",
        help="The databricks API host.",
    )
    parser.add_argument(
        "-t",
        "--token",
        type=str,
        default="",
        help="An authentication token.",
    )
    parser.add_argument(
        "-tcp",
        "--token-cerberus-path",
        type=str,
        default="",
        help="An authentication token.",
    )
    parser.add_argument(
        "-tk",
        "--task-key",
        default=[],
        action="append",
        help=(
            "If provided, only tasks with the specified keys will be updated."
        ),
    )
    parser.add_argument(
        "job-name",
        nargs="*",
        default=[],
        help="The name of the jobs to update.",
    )
    namespace: argparse.Namespace
    namespace = parser.parse_args()
    job_names: Tuple[str, ...] = tuple(getattr(namespace, "job-name"))
    requirements: str = namespace.requirements
    task_keys: Tuple[str, ...] = tuple(namespace.task_key)
    update_jobs_libraries(
        **({"job_names": job_names} if job_names else {}),
        **({"requirements": requirements} if requirements else {}),
        **({"task_keys": task_keys} if task_keys else {}),
        **({"host": namespace.host} if namespace.host else {}),
        **({"token": namespace.token} if namespace.token else {}),
        **(
            {"token_cerberus_path": namespace.token_cerberus_path}
            if namespace.token_cerberus_path
            else {}
        ),
    )


if __name__ == "__main__":
    main()
