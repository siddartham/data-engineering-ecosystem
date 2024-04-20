import re
import sys
import unittest
from datetime import datetime
from itertools import chain
from shutil import which
from subprocess import check_call, check_output
from typing import Iterable, Tuple

import sob
from sqlalchemy.engine import Connection  # type: ignore
from sqlalchemy.engine.row import Row  # type: ignore

from my_materialize_snowflake_views.broker import (
    Broker,
    get_connection_select_statement,
)

ECHO: bool = False


def iter_updated_table_names() -> Iterable[str]:
    """
    Yield the names of all tables which have been updated in the current
    branch.
    """
    git: str = which("git") or "git"
    origin: str = (
        check_output((git, "remote"), encoding="utf-8").strip().split("\n")[0]
    )
    # Fetch the master branch
    check_call((git, "fetch", origin, "main"))
    # Compare the current branch w/ the main branch
    diff: str = check_output(  # type: ignore
        (git, "diff", "--stat", f"{origin}/main"),
        encoding="utf-8",
    )
    print(repr(diff))
    yield from re.findall(r"/([A-za-z_]+)\.sql\b", diff)


class TestBroker(unittest.TestCase):
    def test_materialize(self) -> None:
        """
        This test materializes snowflake views in DEV (because Snowflake
        doesn't provide any means of testing in a local container)
        """
        updated_table_names: Tuple[str, ...] = tuple(
            iter_updated_table_names()
        )
        command: Tuple[str, ...] = (
            f"{sys.executable}",
            "-m",
            "my_materialize_snowflake_views",
            "map-dev",
        )
        if ECHO:
            command += ("-e",)
        if updated_table_names:
            # If SQL has been updated, only test population of the edited
            # tables
            command += tuple(
                chain(
                    *map(
                        lambda table_name: ("--include", table_name),
                        updated_table_names,
                    )
                )
            )
        else:
            # The following is to exclude excessively long-running queries
            # (these will still be validated in QA during deployment)
            command += tuple(
                chain(
                    *map(
                        lambda table_name: ("--exclude", table_name),
                        (
                            "REFURB_SALES_SUSTAINABILITY_MV",
                            "ONEBOX_SUSTAINABILITY_MV",
                            "ONEBOX_BOOKINGS_SUSTAINABILITY_MV",
                            "GOODS_AT_CONSOLIDATOR_PRODUCT_FACTORY_PLANNING_"
                            "SEASON_YEAR_MV",
                        ),
                    )
                )
            )
        check_call(command)

    def test_change_tracking(self) -> None:
        connection: Connection = Broker(
            "map-prod"
        ).work.snowflake_session.bind.connect()
        select_statement: str = get_connection_select_statement(
            connection,
            "STYLE_SEASON_YEAR_SUSTAINABILITY_MV",
        )
        try:
            row: Row = next(connection.exec_driver_sql(select_statement))
            assert isinstance(row["CHANGED"], datetime)
        except Exception as error:
            # Append the select statement to the error message
            sob.errors.append_exception_text(error, f"\n\n{select_statement}")
            raise error


if __name__ == "__main__":
    # unittest.main()
    print(tuple(iter_updated_table_names()))
