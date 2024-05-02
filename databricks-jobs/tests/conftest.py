import sys
from typing import Iterable, cast

import pytest
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.compute import AutoScale, ClusterSpec
from databricks.sdk.service.jobs import (
    BaseJob,
    CreateResponse,
    PythonWheelTask,
    Task,
)

from databricks_jobs.client import get_workspace_client


@pytest.fixture(autouse=True, name="job_name", scope="session")
def create_job() -> Iterable[str]:
    """
    Create a job for testing purposes, then delete the job after tests
    have completed
    """
    name: str = (
        "databricks-jobs-test-py"
        f"{sys.version_info.major}{sys.version_info.minor}"
    )
    client: WorkspaceClient = get_workspace_client()
    # Delete any pre-existing job with this name
    job: BaseJob
    for job in client.jobs.list(name=name):
        client.jobs.delete(job_id=cast(int, job.job_id))
    # Create a new job
    response: CreateResponse
    job_id: int = cast(
        int,
        client.jobs.create(
            name=name,
            tasks=[
                Task(
                    task_key="main",
                    python_wheel_task=PythonWheelTask(
                        package_name="pip",
                        entry_point="pip",
                        parameters=["-h"],
                    ),
                    new_cluster=ClusterSpec(
                        spark_version="14.3.x-scala2.12",
                        spark_conf={
                            "spark.master": "local[*, 4]",
                            "spark.databricks.cluster.profile": "singleNode",
                        },
                        node_type_id="m6g.large",
                        driver_node_type_id="m6g.large",
                        enable_elastic_disk=True,
                        autoscale=AutoScale(min_workers=1, max_workers=1),
                    ),
                )
            ],
        ).job_id,
    )
    yield name
    # Teardown
    try:
        client.jobs.delete(job_id=job_id)
    except Exception:
        pass
