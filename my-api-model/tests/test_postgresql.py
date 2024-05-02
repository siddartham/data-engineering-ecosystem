import os
import unittest
from time import sleep
from typing import Any, Union

from daves_dev_tools.utilities import run
from analytics_orm.postgresql import (
    get_local_docker_user_password_host_port_database,
)
from analytics_orm.validation import validate
from sqlalchemy import text  # type: ignore
from sqlalchemy.engine import Connection, Engine, Row  # type: ignore

from my_api_model.base import Base
from my_api_model.dialects.postgresql import (
    create_environment,
)

TESTS_DIRECTORY: str = os.path.abspath(os.path.dirname(__file__))


def _verify_tables_exist(bind: Union[Engine, Connection]) -> None:
    def get_first_column_value(row: Row) -> str:
        return row[0]

    connection: Connection
    if isinstance(bind, Connection):
        connection = bind
    else:
        connection = bind.connect()
    assert "BUILD_OF_MATERIAL_SEASON_YEAR" in map(
        get_first_column_value,
        connection.execute(
            text("select table_name from information_schema.tables"), ()
        ),
    )


def _verify_views_exist(bind: Union[Engine, Connection]) -> None:
    def get_first_column_value(row: Row) -> str:
        return row[0]

    connection: Connection
    if isinstance(bind, Connection):
        connection = bind
    else:
        connection = bind.connect()
    assert "PRODUCT_SUSTAINABILITY_API_V" in map(
        get_first_column_value,
        connection.execute(
            text("select table_name from information_schema.views"), ()
        ),
    )


class TestPostgreSQL(unittest.TestCase):
    """
    Test this model with PostgreSQL
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        run(
            "docker-compose"
            f" -f '{TESTS_DIRECTORY}/docker-compose.yml'"
            f" --project-directory '{TESTS_DIRECTORY}'"
            " up"
            " -d"
        )
        sleep(10)
        super().__init__(*args, **kwargs)

    def test_create(self) -> None:
        """
        Make sure creating/re-creating the database can be done without
        errors.
        """
        engine: Engine
        index: int
        for index in range(2):
            user: str
            password: str
            host: str
            port: int
            database: str
            (
                user,
                password,
                host,
                port,
                database,
            ) = get_local_docker_user_password_host_port_database()
            engine = create_environment(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database,
                echo=True,
                checkfirst=True,
            )
            _verify_tables_exist(engine)
            _verify_views_exist(engine)
        # Ensure creating only views works
        Base.metadata.create_views(bind=engine)
        validate(Base, engine)

    def __del__(self) -> None:
        run(
            "docker-compose"
            f" -f '{TESTS_DIRECTORY}/docker-compose.yml'"
            f" --project-directory '{TESTS_DIRECTORY}'"
            " down"
        )


if __name__ == "__main__":
    unittest.main()
