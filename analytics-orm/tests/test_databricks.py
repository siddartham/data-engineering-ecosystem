import unittest

from databricks.sdk import WorkspaceClient  # type: ignore
from databricks.sdk.service.compute import (  # type: ignore
    ClusterDetails,
    State,
    Wait,
)
from delta import configure_spark_with_delta_pip
from cerberus_assistant.get import get_secret
from pyspark.sql import SparkSession  # type: ignore
from pyspark.sql.dataframe import DataFrame  # type: ignore
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.url import URL  # type: ignore

from analytics_orm.databricks import create_engine
from analytics_orm.utilities import get_bind_schema

SERVICE_PRINCIPAL_CERBERUS_SECRET_PATH: str = (
    "app/sustainability/sustainability/ServicePrincipal."
    "cloud.databricks.com_App.community.Developer"
)
WAREHOUSE_HTTP_PATH: str = "/sql/1.0/warehouses/123143ffff4445"
SCHEMA: str = "sustainability_dev"
CLUSTER_ID: str = "1234-345678-y4u4czhv"
ORG_ID: str = "1234556789"


def test_cluster_connection() -> None:
    access_token: str = get_secret(SERVICE_PRINCIPAL_CERBERUS_SECRET_PATH)
    workspace_client: WorkspaceClient = WorkspaceClient(
        host="community.cloud.databricks.com",
        token=get_secret(SERVICE_PRINCIPAL_CERBERUS_SECRET_PATH),
    )
    test_cluster: ClusterDetails = workspace_client.clusters.get(CLUSTER_ID)
    waited_cluster: Wait[ClusterDetails]
    if test_cluster.state == State.TERMINATED:
        print("Cluster was stopped, starting now..")
        waited_cluster = workspace_client.clusters.start(CLUSTER_ID)
        assert waited_cluster.result().state == State.RUNNING
    engine: Engine = create_engine(
        schema=SCHEMA,
        http_path=f"/sql/protocolv1/o/{ORG_ID}/{CLUSTER_ID}",
        access_token=access_token,
    )
    connection: Connection = engine.connect()
    assert "information_schema" in map(
        lambda row: row[0],
        connection.exec_driver_sql("show schemas in development"),
    )


def test_warehouse_connection(databricks_dev_connection: Connection) -> None:
    assert "information_schema" in map(
        lambda row: row[0],
        databricks_dev_connection.exec_driver_sql(
            "show schemas in development"
        ),
    )


def test_get_databricks_spark_dataframe(
    databricks_dev_connection: Connection,
) -> None:
    url: URL = databricks_dev_connection.engine.url
    schema: str = get_bind_schema(databricks_dev_connection) or "default"
    data_frame: DataFrame = (
        configure_spark_with_delta_pip(
            SparkSession.builder.config(
                "spark.sql.extensions",
                "io.delta.sql.DeltaSparkSessionExtension",
            ).config(
                "spark.sql.catalog.spark_catalog",
                "org.apache.spark.sql.delta.catalog.DeltaCatalog",
            )
        )
        .getOrCreate()
        .read.jdbc(
            url=f"jdbc:databricks://{url.host}:{url.port or 443}/{schema}",
            table="calculator",
            properties=dict(
                UID=url.username,
                PWD=url.password,
                SSL="1",
                transportMode="http",
                AuthMech="3",
                ConnCatalog=url.query.get("catalog", ""),
                ConnSchema=schema,
                httpPath=url.query.get("http_path", ""),
            ),
        )
    )
    assert isinstance(data_frame, DataFrame)
