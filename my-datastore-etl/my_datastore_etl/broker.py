import tempfile
from datetime import datetime
from logging import Logger
from typing import Any, Dict, FrozenSet, List, Optional, Tuple, Type, Union

import file_system_client.s3 as s3
from etl_framework.broker import WORK_SLOTS as _WORK_SLOTS
from etl_framework.broker import Broker as _Broker
from etl_framework.broker import Work as _Work
from etl_framework.broker import (
    has_databricks_extra,
    has_postgresql_extra,
    has_snowflake_extra,
)
from etl_framework.concurrency import Concurrency
from etl_framework.utilities import call_arguments, get_print_logger
from orm_framework.declarative import Base as ORMBase
from orm_framework.utilities import apply_environment_defaults
from file_system_client.base import FileSystem
from file_system_client.dbfs import DatabricksFileSystem
from file_system_client.local import Local
from my_datastore_orm.base import Base as APIBase
from my_datastore_orm.base import Base
from my_datastore_orm.dialects.s3 import ENVIRONMENTS_URLS

SNOWFLAKE_S3_STAGE_NAME: str = "STAGE.S3_SUSTAINABILITY"

_LOCAL_CONSOLIDATE_DONT_RAISE_EXCEPTIONS: Tuple[Type[Exception], ...] = ()
try:
    from py4j.protocol import Py4JJavaError  # type: ignore

    _LOCAL_CONSOLIDATE_DONT_RAISE_EXCEPTIONS = (Py4JJavaError,)
except ImportError:
    pass

__all__: List[str] = [
    "ENVIRONMENTS",
    "Broker",
    "Work",
    "SOLE_FILE_SYSTEM_ROOT",
]

ENVIRONMENTS: FrozenSet[str] = frozenset(
    (
        "local",
        "sole-dev",
        "sole-qa",
        "sole-prod",
        "map-dev",
        "map-qa",
        "map-prod",
    )
)
SOLE_FILE_SYSTEM_ROOT: str = (
    "/Volumes/development/team_sustainability/waffle_window/"
)


def _get_map_environment_sustainability_s3_arn(environment: str) -> str:
    """
    Retrieve the ARN needed for S3 access to our waffle iron bucket
    """
    environment = environment.rpartition("-")[-1].lower()
    assert environment in ("dev", "qa", "prod")
    return f"arn:aws:iam::567546912947:role/map-{environment}"


def get_environment_file_system(environment: str) -> FileSystem:
    """
    Get an instance of a sub-class of
    `file_system_client.base.FileSystem` representing the given
    `environment`
    """
    if environment == "local":
        # Local testing
        working_path: str = tempfile.mkdtemp()
        return Local(root=f"{working_path}/")
    elif environment.startswith("sole-"):
        environment = environment.rpartition("-")[-1]
        return DatabricksFileSystem(
            root=f"{SOLE_FILE_SYSTEM_ROOT}{environment}/"
        )
    elif environment.startswith("map-"):
        environment = environment.rpartition("-")[-1]
        return s3.from_url(
            ENVIRONMENTS_URLS[environment],
            arn=_get_map_environment_sustainability_s3_arn(environment),
        )
    else:
        return s3.from_url(ENVIRONMENTS_URLS[environment])


def get_environment_snowflake_connection_string(environment: str) -> str:
    """
    Get a Snowflake connection string for the given `environment`
    """
    if not has_snowflake_extra:
        return ""
    from my_datastore_orm.dialects import snowflake

    if environment == "local":
        # For local unit-testing, allow read-only interactions with QA
        return snowflake.get_environment_connection_url(
            role="GSA_FOUNDATION_READ_QA"
        ).render_as_string(False)
    else:
        environment = environment.rpartition("-")[-1].lower()
        assert environment in snowflake.ENVIRONMENTS
        return snowflake.get_environment_connection_url(
            role=("GSA_FOUNDATION_READWRITE_" f"{environment.upper()}")
        ).render_as_string(False)


def get_environment_databricks_connection_string(environment: str) -> str:
    """
    Get a Databricks connection string for the given `environment`
    """
    if not has_databricks_extra:
        return ""
    from my_datastore_orm.dialects import databricks

    if environment == "local":
        # TODO: local delta lake unit testing
        return ""
    else:
        environment = environment.rpartition("-")[-1].lower()
        assert environment in databricks.ENVIRONMENTS
        return databricks.get_environment_connection_url(
            environment
        ).render_as_string(False)


def get_environment_postgresql_connection_string(environment: str) -> str:
    if not has_postgresql_extra:
        return ""
    from orm_framework import postgresql as orm_postgresql
    from my_datastore_orm.dialects import postgresql

    if environment == "local":
        # For unit-testing
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
        ) = orm_postgresql.get_local_docker_user_password_host_port_database()
        return postgresql.get_environment_connection_string(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
        )
    else:
        environment = environment.rpartition("-")[-1].lower()
        assert environment in postgresql.ENVIRONMENTS
        return postgresql.get_environment_connection_string(
            environment=environment
        )


LOCAL_DEFAULTS: Dict[str, Any] = {
    "file_system": lambda: get_environment_file_system("local"),
    "databricks_connection_string": lambda: (
        get_environment_databricks_connection_string("local")
    ),
    "snowflake_connection_string": lambda: (
        get_environment_snowflake_connection_string("local")
    ),
    "postgresql_connection_string": lambda: (
        get_environment_postgresql_connection_string("local")
    ),
    "consolidate_dont_raise_exceptions": (
        _LOCAL_CONSOLIDATE_DONT_RAISE_EXCEPTIONS
    ),
}
SOLE_DEV_DEFAULTS: Dict[str, Any] = {
    "file_system": lambda: get_environment_file_system("sole-dev"),
    "databricks_connection_string": lambda: (
        get_environment_databricks_connection_string("sole-dev")
    ),
    "snowflake_connection_string": lambda: (
        get_environment_snowflake_connection_string("sole-dev")
    ),
    "postgresql_connection_string": lambda: (
        get_environment_postgresql_connection_string("sole-dev")
    ),
    "concurrency": Concurrency.SPARK,
}
SOLE_QA_DEFAULTS: Dict[str, Any] = {
    "file_system": lambda: get_environment_file_system("sole-qa"),
    "databricks_connection_string": lambda: (
        get_environment_databricks_connection_string("sole-qa")
    ),
    "snowflake_connection_string": lambda: (
        get_environment_snowflake_connection_string("sole-qa")
    ),
    "postgresql_connection_string": lambda: (
        get_environment_postgresql_connection_string("sole-qa")
    ),
    "concurrency": Concurrency.SPARK,
}
SOLE_PROD_DEFAULTS: Dict[str, Any] = {
    "file_system": lambda: get_environment_file_system("sole-prod"),
    "databricks_connection_string": lambda: (
        get_environment_databricks_connection_string("sole-prod")
    ),
    "snowflake_connection_string": lambda: (
        get_environment_snowflake_connection_string("sole-prod")
    ),
    "postgresql_connection_string": lambda: (
        get_environment_postgresql_connection_string("sole-prod")
    ),
    "concurrency": Concurrency.SPARK,
}
MAP_DEV_DEFAULTS: Dict[str, Any] = {
    "file_system": lambda: get_environment_file_system("map-dev"),
    "databricks_connection_string": lambda: (
        get_environment_databricks_connection_string("map-dev")
    ),
    "snowflake_connection_string": lambda: (
        get_environment_snowflake_connection_string("map-dev")
    ),
    "postgresql_connection_string": lambda: (
        get_environment_postgresql_connection_string("map-dev")
    ),
}
MAP_QA_DEFAULTS: Dict[str, Any] = {
    "file_system": lambda: get_environment_file_system("map-qa"),
    "databricks_connection_string": lambda: (
        get_environment_databricks_connection_string("map-qa")
    ),
    "snowflake_connection_string": lambda: (
        get_environment_snowflake_connection_string("map-qa")
    ),
    "postgresql_connection_string": lambda: (
        get_environment_postgresql_connection_string("map-qa")
    ),
}
MAP_PROD_DEFAULTS: Dict[str, Any] = {
    "file_system": lambda: get_environment_file_system("map-prod"),
    "databricks_connection_string": lambda: (
        get_environment_databricks_connection_string("map-prod")
    ),
    "snowflake_connection_string": lambda: (
        get_environment_snowflake_connection_string("map-prod")
    ),
    "postgresql_connection_string": lambda: (
        get_environment_postgresql_connection_string("map-prod")
    ),
}


log: Logger = get_print_logger(__name__)

WORK_SLOTS: Tuple[str, ...] = _WORK_SLOTS + ("environment",)


class Work(_Work):

    __slots__: Tuple[str, ...] = WORK_SLOTS

    def __init__(
        self,
        environment: str = "",
        file_system: Optional[FileSystem] = None,
        databricks_base: Optional[Type[ORMBase]] = Base,
        snowflake_base: Optional[Type[ORMBase]] = Base,
        postgresql_base: Optional[Type[ORMBase]] = APIBase,
        postgresql_connection_string: str = "",
        snowflake_connection_string: str = "",
        databricks_connection_string: str = "",
        tables_directory: str = "tables/",
        temp_directory: str = "temp/",
        snowflake_s3_stage_name: str = SNOWFLAKE_S3_STAGE_NAME,
        started: Optional[datetime] = None,
        echo: bool = False,
    ) -> None:
        self.environment: str = environment
        super().__init__(
            file_system=file_system,
            databricks_base=databricks_base,
            snowflake_base=snowflake_base,
            postgresql_base=postgresql_base,
            postgresql_connection_string=postgresql_connection_string,
            snowflake_connection_string=snowflake_connection_string,
            databricks_connection_string=databricks_connection_string,
            tables_directory=tables_directory,
            temp_directory=temp_directory,
            snowflake_s3_stage_name=snowflake_s3_stage_name,
            started=started,
            echo=echo,
        )


class Broker(_Broker):

    work: Work

    @apply_environment_defaults("local", **LOCAL_DEFAULTS)
    @apply_environment_defaults("sole-dev", **SOLE_DEV_DEFAULTS)
    @apply_environment_defaults("sole-qa", **SOLE_QA_DEFAULTS)
    @apply_environment_defaults("sole-prod", **SOLE_PROD_DEFAULTS)
    @apply_environment_defaults("map-dev", **MAP_DEV_DEFAULTS)
    @apply_environment_defaults("map-qa", **MAP_QA_DEFAULTS)
    @apply_environment_defaults("map-prod", **MAP_PROD_DEFAULTS)
    @call_arguments
    def __init__(
        self,
        environment: str,
        file_system: FileSystem,
        parallelism: Optional[int] = None,
        concurrency: Concurrency = Concurrency.MULTIPROCESSING,
        databricks_base: Optional[Type[ORMBase]] = Base,
        snowflake_base: Optional[Type[ORMBase]] = Base,
        postgresql_base: Optional[Type[ORMBase]] = APIBase,
        postgresql_connection_string: str = "",
        snowflake_connection_string: str = "",
        databricks_connection_string: str = "",
        tables_directory: str = "tables/",
        temp_directory: str = "temp/",
        snowflake_s3_stage_name: str = SNOWFLAKE_S3_STAGE_NAME,
        started: Optional[datetime] = None,
        echo: bool = False,
        work: Union[_Work, Type[_Work]] = Work,
        consolidate_dont_raise_exceptions: Tuple[Type[Exception], ...] = (),
    ) -> None:
        assert environment in ENVIRONMENTS
        super().__init__(
            file_system=file_system,
            parallelism=parallelism,
            concurrency=concurrency,
            databricks_base=databricks_base,
            snowflake_base=snowflake_base,
            postgresql_base=postgresql_base,
            postgresql_connection_string=postgresql_connection_string,
            snowflake_connection_string=snowflake_connection_string,
            databricks_connection_string=databricks_connection_string,
            tables_directory=tables_directory,
            temp_directory=temp_directory,
            snowflake_s3_stage_name=snowflake_s3_stage_name,
            started=started,
            echo=echo,
            work=work,
            consolidate_dont_raise_exceptions=(
                consolidate_dont_raise_exceptions
            ),
        )
        self.work.environment = environment
