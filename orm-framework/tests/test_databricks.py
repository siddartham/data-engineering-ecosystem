import unittest

from databricks.sdk import WorkspaceClient  # type: ignore
from databricks.sdk.service.compute import (  # type: ignore
    ClusterDetails,
    State,
    Wait,
)
from orm_framework.databricks import create_engine
from orm_framework.utilities import lru_cache
from orm_framework.cerberus_assistant.get import get_secret
from sqlalchemy.engine.base import Connection, Engine  # type: ignore

SERVICE_PRINCIPAL_CERBERUS_SECRET_PATH: str = (
    "app/org/ServicePrincipal."
    "cloud.databricks.com.Developer"
)

DEVELOPMENT_SCHEMA: str = "dev"
TEST_CLUSTER_ID: str = "awararaw"
DATABRICKS_WORKSPACE_ID: str = "12345567890"


class TestDatabricks(unittest.TestCase):
    @property
    def access_token(self) -> str:
        return get_secret(SERVICE_PRINCIPAL_CERBERUS_SECRET_PATH)

    @property
    @lru_cache()
    def workspace_client(self) -> WorkspaceClient:
        workspace_client: WorkspaceClient = WorkspaceClient(
            host="community.cloud.databricks.com",
            token=self.access_token,
        )

        return workspace_client

    @property
    @lru_cache()
    def bind(self) -> Connection:
        engine: Engine
        workspace_client: WorkspaceClient = self.workspace_client
        test_cluster: ClusterDetails = workspace_client.clusters.get(
            TEST_CLUSTER_ID
        )
        waited_cluster: Wait[ClusterDetails]
        if test_cluster.state == State.TERMINATED:
            print("Cluster was stopped, starting now..")
            waited_cluster = workspace_client.clusters.start(TEST_CLUSTER_ID)

            assert waited_cluster.result().state == State.RUNNING

        engine = create_engine(
            schema=DEVELOPMENT_SCHEMA,
            http_path=f"/sql/protocolv1/o/{SOLE_ORG_ID}/{TEST_CLUSTER_ID}",
            access_token=self.access_token,
        )

        return engine.connect()

    def test_create_engine(self) -> None:
        assert "information_schema" in map(
            lambda row: row[0],
            self.bind.exec_driver_sql("show schemas in development"),
        )
