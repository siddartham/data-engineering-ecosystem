import argparse
from typing import List, Optional, Sequence, Tuple, cast

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.compute import (
    ClusterSpec,
    InitScriptInfo,
    WorkspaceStorageInfo,
)
from databricks.sdk.service.jobs import BaseJob, JobCluster, JobSettings, Task

from ._utilities import apply_defaults
from .client import get_workspace_client
from .config import DEFAULT_HOST, get_pyproject_arguments
from .utilities import list_jobs


def _get_job_cluster_spec(
    job: BaseJob,
    job_cluster_key: str,
) -> ClusterSpec:
    """
    Get the cluster spec for a job cluster ID from a list of job clusters
    """
    job_cluster: JobCluster
    return next(
        filter(
            lambda job_cluster: (
                job_cluster.job_cluster_key == job_cluster_key
            ),
            cast(JobSettings, job.settings).job_clusters or (),
        )
    ).new_cluster


def _get_job_task_cluster_spec(job: BaseJob, task: Task) -> ClusterSpec:
    cluster_spec: Optional[ClusterSpec] = (
        task.new_cluster or _get_job_cluster_spec(job, task.job_cluster_key)
        if task.job_cluster_key
        else task.new_cluster if task.new_cluster else None
    )
    if cluster_spec is None:
        raise RuntimeError(f"No cluster spec was found for the task: {task}.")
    return cluster_spec


@apply_defaults(**get_pyproject_arguments())
def update_jobs_init_scripts(
    job_names: Sequence[str] = (),
    init_scripts: Sequence[str] = (),
    task_keys: Tuple[str, ...] = (),
    host: str = DEFAULT_HOST,
    token: str = "",
    token_cerberus_path: str = "",
) -> None:
    """
    This function updates init scripts for one or more databricks job.
    All init scripts must have been previously uploaded to the workspace.

    Parameters:

    - job_names ([str]|str): The name of the job (or jobs) to update.
    - init_scripts ([str]|str): The worksapce path to one or more init scripts.
    - host (str): The databricks API host.
    - task_keys ((str,)) = (): If provided only tasks with the specified
      keys will be updated.
    - token (str): An authentication token.
    - token_cerberus_path (str): A Cerberus secure drop box path from
      which an authentication token can be retrieved.
    """
    if isinstance(job_names, str):
        job_names = (job_names,)
    if isinstance(init_scripts, str):
        init_scripts = (init_scripts,)
    else:
        # Filter out empty strings
        init_scripts = tuple(filter(None, init_scripts))
    jobs: Tuple[BaseJob, ...] = list_jobs(
        names=job_names,
        host=host,
        token=token,
        token_cerberus_path=token_cerberus_path,
    )
    if not jobs:
        raise ValueError(f"No jobs with the names f{job_names} were found.")
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
                cluster_spec: ClusterSpec = _get_job_task_cluster_spec(
                    job, task
                )
                init_script: str
                cluster_spec.init_scripts = [
                    InitScriptInfo(
                        workspace=WorkspaceStorageInfo(destination=init_script)
                    )
                    for init_script in init_scripts
                ]
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
        prog="databricks-jobs update-init-scripts",
        description=(
            "This command updates init scripts for one or more "
            "databricks job(s). All init scripts must have been "
            "previously uploaded to the workspace."
        ),
    )
    parser.add_argument(
        "-is",
        "--init-script",
        type=str,
        action="append",
        default=[],
        help=(
            "The workspace path to one or more init scripts. If not provided, "
            "or an empty string is provided, all init scripts will be removed "
            "from the specified jobs/tasks."
        ),
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
    init_scripts: Tuple[str, ...] = tuple(namespace.init_script)
    task_keys: Tuple[str, ...] = tuple(namespace.task_key)
    update_jobs_init_scripts(
        **({"job_names": job_names} if job_names else {}),
        **({"init_scripts": init_scripts} if init_scripts else {}),
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
