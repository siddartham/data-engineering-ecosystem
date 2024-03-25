from datetime import datetime, timedelta
from functools import wraps
from typing import IO, Any, Dict, List, Optional

import pendulum  # type: ignore
from airflow.configuration import conf  # type: ignore
from airflow.exceptions import AirflowConfigException  # type: ignore
from airflow.providers.databricks.hooks import databricks_base  # type: ignore
from airflow.providers.databricks.operators.databricks import (  # type: ignore
    DatabricksSubmitRunOperator,
)

from airflow import DAG  # type: ignore

CERBERUS_URL: str = "https://prod.cerberus.mycloud.com"
DATABRICKS_HOST: str = "community.cloud.databricks.com"
ENVIRONMENT: str
try:
    ENVIRONMENT = conf.get("compute", "env") or ""
except AirflowConfigException:
    # This facilitates static analysis of the DAG
    ENVIRONMENT = "dev"
NAME: str = "my-sample-etl"
PACKAGE: str = "my_sample_etl"
ENTRY_POINT: str = NAME


@wraps(databricks_base.BaseDatabricksHook._get_token)
def get_service_principal_token(
    self: databricks_base.BaseDatabricksHook, raise_error: bool = False
) -> str:
    """
    The CerberusClient import needs to be included within this function or
    airflow won't permit importing the DAG
    """
    from cerberus.client import CerberusClient  # type: ignore

    return CerberusClient(CERBERUS_URL).get_secret(
        secure_data_path="app/sustainability/sustainability",
        key=(
            "databricks"
            ".cloud.databricks.com_App.mydatastore.Developer"
        ),
    )


databricks_base.BaseDatabricksHook._get_token = (  # type: ignore
    get_service_principal_token
)
databricks_base.BaseDatabricksHook.host = DATABRICKS_HOST  # type: ignore


def get_start_date() -> datetime:
    return (
        pendulum.now(tz="America/Los_Angeles").replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        - timedelta(days=2)  # noqa W503
    ).astimezone(pendulum.tz.UTC)


def get_schedule_interval() -> Optional[str]:
    interval: Optional[str] = None
    return interval


with DAG(
    dag_id="enablon_conversion_etl_sole",
    start_date=get_start_date(),
    schedule_interval=get_schedule_interval(),
) as dag:
    libraries: List[Dict[str, Any]] = []
    requirements_io: IO[str]
    with open(
        "/usr/local/airflow/code/sample_etl_requirements.txt"
    ) as requirements_io:
        package: str
        for package in requirements_io.read().strip().split("\n")[1:]:
            libraries.append(
                {
                    "pypi": {
                        "package": package,
                    }
                }
            )
    DatabricksSubmitRunOperator(
        dag=dag,
        task_id=f"{NAME}-{ENVIRONMENT}",
        # https://docs.databricks.com/api/workspace/jobs/submit
        json={
            "tasks": [
                {
                    "task_key": NAME,
                    "python_wheel_task": {
                        "package_name": PACKAGE,
                        "entry_point": ENTRY_POINT,
                        "parameters": [
                            f"sole-{ENVIRONMENT}",
                            "-p",
                            "16",
                            "-e",
                        ],
                    },
                    "new_cluster": {
                        "spark_version": "13.2.x-scala2.12",
                        "spark_conf": {
                            "spark.dynamicAllocation.executorIdleTimeout": (
                                "3600000"
                            ),
                            "spark.yarn.am.waitTime": "3600000",
                            # Enable Unity Catalog Volumes (UC Volumes)
                            "spark.databricks.unityCatalog.volumes.enabled": (
                                "true"
                            ),
                            (
                                "spark.databricks.unityCatalog.volumes.fuse."
                                "server.enabled"
                            ): "true",
                        },
                        "aws_attributes": {
                            "first_on_demand": 9,
                            "availability": "ON_DEMAND",
                            "ebs_volume_count": 1,
                            "ebs_volume_size": 100,
                        },
                        "node_type_id": "r6g.large",
                        "driver_node_type_id": "r6g.xlarge",
                        "num_workers": 1,
                        "policy_id": "E0641B99CA00001B",
                        "autoscale": {"min_workers": 1, "max_workers": 8},
                        "custom_tags": {
                            "environment": ENVIRONMENT,
                        },
                    },
                    "libraries": libraries,
                },
            ],
            # The active directory groups, users, or principals which
            # should have access to this job
            "access_control_list": [
                {
                    "group_name": "App.Org.org.Developer",
                    "permission_level": "CAN_MANAGE",
                },
                {
                    "group_name": "App.Org.org.DataAdmin",
                    "permission_level": "CAN_MANAGE",
                },
            ],
        },
    )
