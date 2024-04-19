import unittest

from cerberus_assistant.get import get_secret
from sqlalchemy.engine import Engine  # type: ignore
from sqlalchemy.sql.expression import text  # type: ignore

from my_datastore_orm.dialects.databricks import (
    create_environment_engine,
)

TEST_CLUSTER_ID: str = "1009-202125-wqc2vk54"
SOLE_ORG_ID: str = "12321423425"

SERVICE_PRINCIPAL_CERBERUS_SECRET_PATH: str = (
    "app/sustainability/sustainability/ServicePrincipal."
    "cloud.databricks.com_App.community.org.Developer"
)


class TestDatabricks(unittest.TestCase):
    """
    Verify that we can connect to Databricks
    """

    @property
    def access_token(self) -> str:
        return get_secret(SERVICE_PRINCIPAL_CERBERUS_SECRET_PATH)

    @property  # type: ignore
    def bind(self) -> Engine:
        return create_environment_engine(
            environment="dev",
            access_token=self.access_token,
            echo=True,
        ).connect()

    def test_schema_exists(self) -> None:
        version: str = self.bind.execute(
            text("select current_version()")
        ).fetchone()[0]
        print(version)
