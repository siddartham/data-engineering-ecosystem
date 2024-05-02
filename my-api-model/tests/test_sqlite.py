import functools
import os
import unittest
from datetime import datetime
from tempfile import gettempdir
from typing import Any, Callable

from daves_dev_tools.utilities import run
from analytics_orm.sqlite import create_engine
from sqlalchemy import text  # type: ignore
from sqlalchemy.engine import Connection, Row  # type: ignore

from my_api_model.base import Base

lru_cache: Callable[..., Any] = functools.lru_cache

DATABASE_PATH: str = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    "data",
    "my_api.sqlite",
)


def _verify_tables_exist(bind: Connection) -> None:
    def get_first_column_value(row: Row) -> str:
        return row[0]

    assert "BUILD_OF_MATERIAL_SEASON_YEAR" in map(
        get_first_column_value,
        bind.execute(text("SELECT name FROM sqlite_master"), ()),
    )


class TestSQLite(unittest.TestCase):
    """
    TODO
    """

    @property  # type: ignore
    @lru_cache()
    def connection(self) -> Connection:
        try:
            os.remove(DATABASE_PATH)
        except FileNotFoundError:
            os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
        return create_engine(path=DATABASE_PATH, echo=True).connect()

    def test_lib_create(self) -> None:
        """
        Make sure creating and re-creating the database can be done
        without errors.
        """
        Base.metadata.create_all(bind=self.connection)
        _verify_tables_exist(self.connection)
        # Ensure re-creation works as well
        Base.metadata.create_all(bind=self.connection, checkfirst=True)
        _verify_tables_exist(self.connection)
        # Ensure creating just views also works
        Base.metadata.create_views(self.connection, checkfirst=True)

    def test_cli_create(self) -> None:
        """
        Make sure creating and re-creating the database can be done
        without errors.
        """
        directory: str = os.path.join(
            gettempdir(), "test-my-api-model"
        )
        path: str = os.path.join(
            directory,
            f"{datetime.now().isoformat(sep='-', timespec='seconds')}.sqlite",
        )
        os.makedirs(directory, exist_ok=True)
        run(("my-api-model", "sqlite", "create", path))
        _verify_tables_exist(create_engine(path=path).connect())
        # Ensure re-creation works as well
        run(f"my-api-model sqlite create {path} -cf")


if __name__ == "__main__":
    unittest.main()
