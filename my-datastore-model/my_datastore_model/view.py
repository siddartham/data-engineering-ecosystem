"""
This module contains utilities for management of views
"""

import os
import re
from typing import IO, Any, Callable, Match, Optional, Union

from sqlalchemy.engine import Connection, Engine  # type: ignore

_has_snowflake_extra: bool = False
get_snowflake_bind_environment: Callable[..., str]
try:
    from .dialects.snowflake import (
        get_bind_environment as get_snowflake_bind_environment,
    )

    _has_snowflake_extra = True
except ImportError:

    def get_snowflake_bind_environment(bind: Any) -> str:
        return ""


_CTE_VIEW_SELECT_PATTERN: str = (
    r"SELECT[\s\n]+\*[\s\n]+FROM[\s\n]+"
    r"\"?(?:PROCESSED|BCL_[A-Za-z0-9_]+)\"?.\"?{}\"?"
)
SNOWFLAKE_VIEW_DIRECTORY: str = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "_snowflake_views",
)


def get_snowflake_view_select_statement(
    view: str, directory: str = SNOWFLAKE_VIEW_DIRECTORY
) -> str:
    """
    Read and return the SQL for a Snowflake view select statement.
    When another view is referenced using the pattern:
    `SELECT * FROM SCHEMA.VIEW_NAME`, the referenced view's
    select statement will be substituted.

    Parameters:

    - view (str)
    """
    if not _has_snowflake_extra:
        return ""
    statement: str
    statement_io: IO[str]
    with open(
        os.path.join(
            directory,
            f"{view}.sql",
        )
    ) as statement_io:
        statement = statement_io.read()
    # Replace CTE `SELECT *` statements
    matched: Match
    for matched in re.finditer(
        _CTE_VIEW_SELECT_PATTERN.format(r"([A-Za-z0-9_]+)"),
        statement,
        flags=re.IGNORECASE,
    ):
        cte_view: str = matched.groups()[0]
        # We look for a view definition first in the explicitly
        # provided location, then in this package's view directory
        for directory_ in (directory,) + (
            ()
            if SNOWFLAKE_VIEW_DIRECTORY == directory
            else (SNOWFLAKE_VIEW_DIRECTORY,)
        ):
            try:
                statement = re.sub(
                    _CTE_VIEW_SELECT_PATTERN.format(cte_view),
                    get_snowflake_view_select_statement(
                        cte_view,
                        directory=directory_,
                    ),
                    statement,
                    flags=re.IGNORECASE,
                )
                break
            except FileNotFoundError:
                # If no SQL file is found for the match, ignore it and continue
                pass
    return statement


def get_bind_snowflake_view_select_statement(
    bind: Union[Connection, Engine],
    view: str,
    directory: str = SNOWFLAKE_VIEW_DIRECTORY,
) -> Optional[str]:
    """
    This function accepts a bind (a SQLAlchemy Engine or Connection object)
    and uses that to determine the appropriate SELECT statement to return
    for the specified `view`.
    """
    if not _has_snowflake_extra:
        return None
    environment: str = get_snowflake_bind_environment(bind)
    # This view is only applicable for Snowflake
    if not environment:
        return None
    # Read the SQL file
    statement: str = get_snowflake_view_select_statement(
        view, directory=directory
    )
    # Use "EDA_PRODUCT_QA" instead of "EDA_PRODUCT_PROD" in
    # non-prod environments
    if environment == "dev":
        statement = re.sub(
            r"\bEDA_PRODUCT_PROD\b",
            "EDA_PRODUCT_QA",
            re.sub(
                r"\bCALENDAR_PROD\b",
                "CALENDAR_DEV",
                re.sub(
                    r"\bMATERIAL_PROD\b",
                    "MATERIAL_QA",
                    statement,
                ),
            ),
        )
    elif environment == "qa":
        statement = re.sub(
            r"\bEDA_PRODUCT_PROD\b",
            "EDA_PRODUCT_QA",
            re.sub(
                r"\bCALENDAR_PROD\b",
                "CALENDAR_QA",
                re.sub(
                    r"\bMATERIAL_PROD\b",
                    "MATERIAL_QA",
                    statement,
                ),
            ),
        )
    else:
        assert environment == "prod"
    return statement
