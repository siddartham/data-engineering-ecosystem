import re
import unittest

from sqlalchemy import text  # type: ignore
from sqlalchemy.engine import Engine  # type: ignore

from my_datastore_orm.dialects.snowflake import (
    create_environment_engine,
)


class TestBroker(unittest.TestCase):
    """
    Verify that we can connect to Snowflake
    """

    @property  # type: ignore
    def bind(self) -> Engine:
        engine = create_environment_engine(
            role="APP_SNOWFLAKE_DEV_ORG_ADMIN"
        )
        return engine.connect()

    def test_select_current_version(self) -> None:
        """
        Verify that we can connect and execute queries
        """
        version: str = self.bind.execute(
            text("select current_version()")
        ).fetchone()[0]
        # Verify the response is a 3-part version string
        assert re.match(r"^\d+\.\d+\.\d+$", version)


if __name__ == "__main__":
    unittest.main()
