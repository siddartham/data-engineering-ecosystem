import os
import sys
from pathlib import Path
from subprocess import check_call
from typing import Tuple

from analytics_orm.alembic.migrations import run
from sqlalchemy.engine import URL, make_url  # type: ignore

import alembic  # type: ignore
from alembic.runtime.environment import EnvironmentContext  # type: ignore
from my_datastore_orm.base import Base
from my_datastore_orm.dialects import databricks, snowflake

context: EnvironmentContext = getattr(alembic, "context")

UPDATE_DICTIONARY_SCRIPT_PATH: Path = (
    Path(__file__)
    .parent.parent.absolute()
    .joinpath("scripts/update_dictionary.py")
)


def get_bind() -> URL:
    """
    Get the bind URL for this session
    """
    sqlalchemy_url: str = (
        context.config.get_main_option("sqlalchemy.url") or ""
    )
    assert sqlalchemy_url
    url: URL = make_url(sqlalchemy_url)
    assert isinstance(url, URL)
    if (url.username and url.password) or url.drivername == "sqlite":
        return url
    elif url.drivername == "snowflake":
        return snowflake.get_environment_connection_url(role=url.query["role"])
    elif url.drivername == "databricks":
        environment: str = context.config.config_ini_section.partition(
            "databricks-"
        )[-1]
        return databricks.get_environment_connection_url(
            environment=environment
        )
    else:
        raise ValueError(url)


def update_dictionary() -> None:
    if os.path.exists(UPDATE_DICTIONARY_SCRIPT_PATH):
        command: Tuple[str, ...] = (
            sys.executable,
            str(UPDATE_DICTIONARY_SCRIPT_PATH),
        )

        check_call(command, universal_newlines=True)


def main() -> None:
    bind: URL = get_bind()
    print(bind)
    run(
        metadata=Base.metadata,
        bind=bind,
        version_table_schema=(
            "COMMON_DIMENSION"
            if bind.drivername.split("+")[0] == "snowflake"
            else None
        ),
    )


main()
update_dictionary()
