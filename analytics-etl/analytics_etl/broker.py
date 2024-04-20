import copyreg
import errno
import functools
import importlib.metadata
import inspect
import itertools
import json
import os
import re
import ssl
import sys
import threading
import weakref
from collections import deque
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from io import BytesIO
from itertools import starmap
from logging import Logger
from multiprocessing import queues
from multiprocessing.pool import Pool
from multiprocessing.util import Finalize, debug, info, is_exiting
from re import Match, Pattern
from subprocess import check_output
from traceback import format_exception
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
    cast,
)
from warnings import warn

import pyarrow  # type: ignore
from analytics_orm.declarative import (
    Base,
    get_base_table_name_subclass,
    get_class_mapper,
    get_class_primary_key_column_names,
    get_class_qualified_table_name,
    get_class_table_name,
    iter_base_sorted_subclasses,
)
from analytics_orm.errors import append_exception_text
from analytics_orm.utilities import lru_cache
from file_system_client import from_url, s3
from file_system_client.base import FileSystem
from file_system_client.errors import get_exception_text
from file_system_client.local import Local
from file_system_client.utilities import (
    get_date_directory_name,
    is_date_partition_directory,
)
from pandas import DataFrame  # type: ignore
from sqlalchemy import Column, DateTime, text  # type: ignore
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.create import create_engine  # type: ignore
from sqlalchemy.engine.interfaces import Dialect  # type: ignore
from sqlalchemy.engine.result import Row  # type: ignore
from sqlalchemy.engine.url import URL  # type: ignore
from sqlalchemy.orm import Session, sessionmaker  # type: ignore
from sqlalchemy.sql.compiler import IdentifierPreparer  # type: ignore
from sqlalchemy.sql.expression import Select, TextClause  # type: ignore
from sqlalchemy.sql.type_api import TypeEngine  # type: ignore
from urllib3 import PoolManager  # type: ignore

from .concurrency import Concurrency
from .utilities import get_print_logger, is_spark_path_not_found_error, retry

has_snowflake_extra: bool = False
try:
    import analytics_orm.snowflake  # noqa

    has_snowflake_extra = True
except ImportError:
    pass
has_databricks_extra: bool = False
try:
    import analytics_orm.databricks  # noqa

    has_databricks_extra = True
except ImportError:
    pass
has_spark_extra: bool = False
try:
    # isort: off
    from analytics_orm.spark import (
        get_data_frame_with_unique_primary_keys,
        get_struct_type_from_mapping,
        merge_data_frames,
    )
    from pyspark import RDD  # type: ignore
    from pyspark.sql import SparkSession  # type: ignore
    from pyspark.sql.dataframe import (  # type: ignore
        DataFrame as SparkDataFrame,
    )
    from pyspark.sql.types import StructType  # type: ignore
    from pyspark.errors.exceptions.captured import (  # type: ignore
        AnalysisException,
    )
    from delta.tables import DeltaMergeBuilder, DeltaTable, DeltaTableBuilder

    # isort: on

    has_spark_extra = True
except ImportError:
    RDD = None  # type: ignore
    SparkSession = None  # type: ignore
    SparkDataFrame = None  # type: ignore
    merge_data_frames = None  # type: ignore
    get_struct_type_from_mapping = None  # type: ignore
    get_data_frame_with_unique_primary_keys = None  # type: ignore
    AnalysisException = None  # type: ignore
    StructType = None  # type: ignore
    DeltaMergeBuilder = None  # type: ignore
    DeltaTableBuilder = None  # type: ignore
    DeltaTable = None  # type: ignore

has_postgresql_extra: bool = False
try:
    import analytics_orm.postgresql  # noqa

    has_postgresql_extra = True
except ImportError:
    pass
__all__: List[str] = [
    "Broker",
    "Work",
    "has_databricks_extra",
    "has_snowflake_extra",
    "has_postgresql_extra",
    "has_spark_extra",
]
log: Logger = get_print_logger(__name__)
# Add typing to our LRU Cache decorators
sqlalchemy_session_lru_cache: Callable[
    ..., Callable[[Callable[["Work"], Session]], Callable[["Work"], Session]]
] = functools.lru_cache  # type: ignore
str_lru_cache: Callable[
    ..., Callable[[Callable[["Work"], str]], Callable[["Work"], str]]
] = functools.lru_cache  # type: ignore
spark_session_lru_cache: Callable[
    ...,
    Callable[[Callable[[str], SparkSession]], Callable[[], SparkSession]],
] = functools.lru_cache  # type: ignore
dict_str_str_lru_cache: Callable[
    ...,
    Callable[
        [Callable[["Work"], Dict[str, str]]],
        Callable[["Work"], Dict[str, str]],
    ],
] = functools.lru_cache  # type: ignore
dict_str_tuple_str_lru_cache: Callable[
    ...,
    Callable[
        [Callable[["Work"], Dict[str, Tuple[str, ...]]]],
        Callable[["Work"], Dict[str, Tuple[str, ...]]],
    ],
] = functools.lru_cache  # type: ignore


def _new_pool_manager(
    num_pools: int,
    headers: Optional[Dict[str, str]],
    connection_pool_kw: Dict[str, Any],
) -> PoolManager:
    return PoolManager(num_pools, headers=headers, **connection_pool_kw)


def _make_pickleable() -> None:
    # This makes it so that thread-locked connections can be pickled
    LockType: type = type(threading.Lock())
    RLockType: type = type(threading.RLock())
    copyreg.pickle(LockType, lambda self: (threading.Lock, ()))  # type: ignore
    copyreg.pickle(
        RLockType, lambda self: (threading.RLock, ())  # type: ignore
    )
    # This makes it so that `ssl.SSLContext` instances can be pickled
    copyreg.pickle(
        ssl.SSLContext,
        lambda self: (ssl.SSLContext, (self.protocol,)),  # type: ignore
    )
    # This makes it so that `urllib3.poolmanager.PoolManager` instances can be
    # pickled
    copyreg.pickle(
        PoolManager,
        lambda self: (
            _new_pool_manager,
            (
                self.pools._maxsize,
                self.headers,
                self.connection_pool_kw,
            ),  # noqa
        ),
    )


_make_pickleable()


@functools.wraps(queues.Queue.close)
def _queue_close(self: queues.Queue) -> None:
    """
    This is a patched version of `multiprocessing.queues.Queue.close` which
    fixes frequent `BrokenPipeError`s
    """
    self._closed = True  # type: ignore
    close: Any = self._close  # type: ignore
    if close:
        self._close = None  # type: ignore
        close()


@functools.wraps(queues.Queue._start_thread)  # type: ignore
def _queueu_start_thread(self: queues.Queue) -> None:
    """
    This is a patched version of `multiprocessing.queues.Queue._start_thread`
    which fixes frequent `BrokenPipeError`s
    """
    debug("Queue._start_thread()")
    # Start thread which transfers data from buffer to pipe
    self._buffer.clear()  # type: ignore
    self._thread = threading.Thread(  # type: ignore
        target=queues.Queue._feed,  # type: ignore
        args=(  # type: ignore
            self._buffer,  # type: ignore
            self._notempty,  # type: ignore
            self._send_bytes,  # type: ignore
            self._wlock,  # type: ignore
            self._reader.close,  # type: ignore
            self._writer.close,  # type: ignore
            self._ignore_epipe,  # type: ignore
            self._on_queue_feeder_error,  # type: ignore
            self._sem,  # type: ignore
        ),
        name="QueueFeederThread",
    )
    self._thread.daemon = True  # type: ignore
    debug("doing self._thread.start()")
    self._thread.start()  # type: ignore
    debug("... done self._thread.start()")
    if not self._joincancelled:  # type: ignore
        self._jointhread = Finalize(  # type: ignore
            self._thread,  # type: ignore
            queues.Queue._finalize_join,  # type: ignore
            [weakref.ref(self._thread)],  # type: ignore
            exitpriority=-5,
        )
    # Send sentinel to the thread queue object when garbage collected
    self._close = Finalize(  # type: ignore
        self,
        queues.Queue._finalize_close,  # type: ignore
        [self._buffer, self._notempty],  # type: ignore
        exitpriority=10,  # type: ignore
    )


def _queueu_feed(  # noqa: C901
    buffer: Any,
    notempty: Any,
    send_bytes: Any,
    writelock: Any,
    reader_close: Any,
    writer_close: Any,
    ignore_epipe: Any,
    onerror: Any,
    queue_sem: Any,
) -> None:
    debug("starting thread to feed data to pipe")
    nacquire = notempty.acquire
    nrelease = notempty.release
    nwait = notempty.wait
    bpopleft = buffer.popleft
    sentinel = queues._sentinel  # type: ignore
    if sys.platform != "win32":
        wacquire = writelock.acquire
        wrelease = writelock.release
    else:
        wacquire = None
    while 1:
        try:
            nacquire()
            try:
                if not buffer:
                    nwait()
            finally:
                nrelease()
            try:
                while 1:
                    obj = bpopleft()
                    if obj is sentinel:
                        debug("feeder thread got sentinel -- exiting")
                        reader_close()
                        writer_close()
                        return
                    # serialize the data before acquiring the lock
                    obj = queues._ForkingPickler.dumps(obj)  # type: ignore
                    if wacquire is None:
                        send_bytes(obj)
                    else:
                        wacquire()
                        try:
                            send_bytes(obj)
                        finally:
                            wrelease()
            except IndexError:
                pass
        except Exception as e:
            if ignore_epipe and getattr(e, "errno", 0) == errno.EPIPE:
                return
            # Since this runs in a daemon thread the resources it uses
            # may be become unusable while the process is cleaning up.
            # We ignore errors which happen after the process has
            # started to cleanup.
            if is_exiting():
                info("error in queue thread: %s", e)
                return
            else:
                # Since the object has not been sent in the queue, we need
                # to decrease the size of the queue. The error acts as
                # if the object had been silently removed from the queue
                # and this step is necessary to have a properly working
                # queue.
                queue_sem.release()
                onerror(e, obj)


def _patch_mutliprocessing_queue() -> None:
    """
    This patch backports a fix for multiprocessing.queues.Queue to prevent
    `BrokenPipeError`s:

    https://github.com/python/cpython/pull/31913
    """
    if (
        sys.version_info[:2] <= (3, 8)
        # For python 3.9, test to see if this is a patch version which has
        # already implemented the fix
        or (
            sys.version_info[:2] <= (3, 9)
            and "try:" in inspect.getsource(queues.Queue.close)
        )
    ):
        queues.Queue.close = _queue_close  # type: ignore
        queues.Queue._start_thread = _queueu_start_thread  # type: ignore
        queues.Queue._feed = _queueu_feed  # type: ignore


_patch_mutliprocessing_queue()


def _get_session(
    base: Type[Base], connection_string: str, echo: bool = False
) -> Session:
    bind: Engine = create_engine(connection_string)
    base.metadata.bind = bind
    base.metadata.bind.echo = echo
    session = sessionmaker(bind=bind)()
    return session


@lru_cache()
def _get_sql_type_instance(
    class_or_instance: Union[Type[TypeEngine], TypeEngine]
) -> TypeEngine:
    if isinstance(class_or_instance, type):
        return class_or_instance()
    else:
        return class_or_instance


def _map_partitions_wrap(function: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(partitioned_args: Iterable[Any]) -> Iterable[Any]:
        arg: Any
        for arg in partitioned_args:
            yield function(arg)

    return wrapper


def _star_map_partitions_wrap(
    function: Callable[..., Any]
) -> Callable[..., Any]:
    def wrapper(partitioned_args: Iterable[Iterable[Any]]) -> Iterable[Any]:
        args: Iterable[Any]
        for args in partitioned_args:
            yield function(*args)

    return wrapper


def _star_map_wrap(function: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(args: Iterable[Any]) -> Any:
        return function(*args)

    return wrapper


def _write_parquet_retry_hook(error: Exception) -> bool:
    assert isinstance(error, RuntimeError)
    return "can't start new thread" in str(error)


@spark_session_lru_cache()
def _get_spark_session(name: str = "analytics-etl") -> SparkSession:
    from delta import configure_spark_with_delta_pip

    if not has_spark_extra:
        raise AttributeError(
            "Use of this property requires installation of the "
            '"spark" extra for analytics-etl:\n'
            "pip3 install 'analytics-etl[spark]'"
        )
    return configure_spark_with_delta_pip(
        SparkSession.builder.appName(name)
        .config(
            "spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension"
        )
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    ).getOrCreate()


def _iter_snowflake_qualified_table_names(base: Type[Base]) -> Iterable[str]:
    """
    Yield all (schema-qualified) Snowflake table names
    """
    cls: Type[Base]
    for cls in iter_base_sorted_subclasses(base):
        if not cls.__table__.info.get("is_view", False):
            yield get_class_qualified_table_name(cls, dialect_name="snowflake")


WORK_SLOTS: Tuple[str, ...] = (
    "file_system",
    "databricks_base",
    "snowflake_base",
    "postgresql_base",
    "snowflake_connection_string",
    "postgresql_connection_string",
    "databricks_connection_string",
    "tables_directory",
    "temp_directory",
    "echo",
    "started",
    "snowflake_s3_stage_name",
)


def _get_first(items: Iterable[Any]) -> Any:
    return next(iter(items))


class Work:
    """
    This class encapsulates work to be performed by individual processes in a
    multi-process pool.

    Parameters:

    - file_system (file_system_client.base.FileSystem)
    - databricks_base (typing.Type[analytics_orm.declarative.Base]|None)
    - snowflake_base (typing.Type[analytics_orm.declarative.Base]|None)
    - postgresql_base (typing.Type[analytics_orm.declarative.Base]|None)
    - postgresql_connection_string (str)
    - snowflake_connection_string (str)
    - databricks_connection_string (str)
      for writing dataframes to s3, in lieu of the file system root
    - started (datetime.datetime|None):
      The date and time at which the job started, for bookmarking purposes.
    - echo (bool)
    """

    __slots__: Tuple[str, ...] = WORK_SLOTS

    def __init__(
        self,
        file_system: Optional[FileSystem] = None,
        databricks_base: Optional[Type[Base]] = None,
        snowflake_base: Optional[Type[Base]] = None,
        postgresql_base: Optional[Type[Base]] = None,
        postgresql_connection_string: str = "",
        snowflake_connection_string: str = "",
        databricks_connection_string: str = "",
        tables_directory: str = "tables/",
        temp_directory: str = "temp/",
        snowflake_s3_stage_name: str = "",
        started: Optional[datetime] = None,
        echo: bool = False,
    ) -> None:
        self.file_system: Optional[FileSystem] = file_system
        self.databricks_base: Optional[Type[Base]] = databricks_base
        self.snowflake_base: Optional[Type[Base]] = snowflake_base
        self.postgresql_base: Optional[Type[Base]] = postgresql_base
        self.snowflake_connection_string: str = snowflake_connection_string
        self.postgresql_connection_string: str = postgresql_connection_string
        self.databricks_connection_string: str = databricks_connection_string
        self.snowflake_s3_stage_name: str = snowflake_s3_stage_name
        assert tables_directory.endswith("/")
        self.tables_directory: str = tables_directory
        self.temp_directory: str = temp_directory
        self.echo: bool = echo
        if not started:
            started = datetime.utcnow()
        self.started: datetime = started

    @property
    @lru_cache(maxsize=1)
    def timestamp(self) -> str:
        return get_date_directory_name(self.started)

    def __getstate__(self) -> Dict[str, Any]:
        """
        Get a dictionary of attributes for pickling
        """
        slot: str
        return dict(
            map(
                lambda slot: (slot, getattr(self, slot)),
                self.__slots__,
            )
        )

    def __setstate__(self, state: Dict[str, Any]) -> None:
        """
        Unpickle an instance of `oapi.client.Client` from a state dictionary
        """
        # Determine which state keys are parameters for the `__init__` method
        parameters: Iterable[
            Tuple[str, inspect.Parameter]
        ] = inspect.signature(
            self.__init__  # type: ignore
        ).parameters.items()
        item: Tuple[str, inspect.Parameter]
        parameter_names: Set[str] = set(
            map(
                _get_first,
                filter(
                    lambda item: item[1].kind
                    not in (
                        inspect.Parameter.VAR_POSITIONAL,
                        inspect.Parameter.POSITIONAL_ONLY,
                    ),
                    parameters,
                ),
            )
        )
        state_keys: Set[str] = set(state.keys())
        kwargs: Dict[str, Any] = {}
        key: str
        value: Any
        for key in state_keys & parameter_names:
            kwargs[key] = state.pop(key)
        self.__init__(**kwargs)  # type: ignore
        # Set the remaining state slots
        deque(map(lambda item: setattr(self, *item), state.items()), maxlen=0)

    @property
    def spark_session(self) -> SparkSession:
        return _get_spark_session()

    @lru_cache()
    def _is_databricks(self) -> bool:
        if not has_spark_extra:
            log.info("Not a Spark job")
            return False
        if self.spark_session.sparkContext.getConf().get(
            "spark.databricks.clusterUsageTags.clusterAllTags", ""
        ):
            log.info("Running a Spark Job on Databricks")
            return True
        log.info("Running a Spark Job, not on Databricks")
        return False

    @property  # type: ignore
    @sqlalchemy_session_lru_cache()
    def databricks_session(self) -> Session:
        """
        This is a SQLAlchemy ORM Session for the Databricks SQL query engine
        """
        if not has_databricks_extra:
            raise AttributeError(
                "Use of this property requires installation of the "
                '"databricks" extra for analytics-etl:\n'
                "pip3 install 'analytics-etl[databricks]'"
            )
        if not self.databricks_connection_string:
            raise AttributeError(
                "You must provide a Databricks connection string"
            )
        if not self.databricks_base:
            raise AttributeError(
                "You must provide a Databricks declarative base"
            )
        if self.echo:
            log.info("Establishing Databricks SQL connection")
        return _get_session(
            base=self.databricks_base,
            connection_string=self.databricks_connection_string,
            echo=self.echo,
        )

    def _validate_databricks_pypi_library_versions(self) -> None:
        """
        This method compares the version of libraries specified in the current
        Databricks job with those installed in the current environment, and
        raises an error if they do not match.
        """

        from databricks.sdk import WorkspaceClient
        from databricks.sdk.service.compute import Library
        from databricks.sdk.service.jobs import RunTask

        # Get the job and run IDs from the cluster name
        cluster_name: str = self.spark_session.conf.get(  # type: ignore
            "spark.databricks.clusterUsageTags.clusterName",
            self.spark_session.sparkContext.getConf().get(
                "spark.databricks.clusterUsageTags.clusterName", ""
            ),
        )
        if cluster_name:
            log.info(f"Cluster Name: {cluster_name}")
            matched: Optional[Match] = _CLUSTER_NAME_JOB_RUN_PATTERN.match(
                cluster_name
            )
            if matched:
                error_message: Set[str] = set()
                url: URL = self.databricks_session.bind.engine.url
                task: RunTask
                for task in (
                    WorkspaceClient(host=url.host, token=url.password)
                    .jobs.get_run(int(matched.group("run_id") or 0))
                    .tasks
                    or ()
                ):
                    library: Library
                    for library in task.libraries or ():
                        if (
                            library.pypi
                            and library.pypi.package
                            and ("==" in library.pypi.package)
                        ):
                            package_name: str
                            library_version: str
                            package_name, library_version = (
                                library.pypi.package.partition("==")[::2]
                            )
                            try:
                                installed_version: str = (
                                    importlib.metadata.version(package_name)
                                )
                                if installed_version != library_version:
                                    error_message.add(
                                        f"{package_name}: "
                                        f"{library_version} "
                                        f"!= {installed_version}"
                                    )
                            except importlib.metadata.PackageNotFoundError:
                                error_message.add(
                                    f"{package_name}: "
                                    f"{library_version} != None"
                                )
                if error_message:
                    raise RuntimeError(
                        "The following PyPI library versions specified in the "
                        "Databricks job do not match the installed package "
                        "version.\n\n"
                        "Package Name: Library Version != Installed Version\n"
                        "{}".format("\n".join(sorted(error_message)))
                    )
                return
            warn(
                "A job ID could not be inferred from the cluster name: "
                f"{cluster_name}"
            )
            return
        warn("No cluster name found")

    @property  # type: ignore
    @sqlalchemy_session_lru_cache()
    def snowflake_session(self) -> Session:
        """
        This is a SQLAlchemy ORM Session for the Snowflake database
        """
        if not has_snowflake_extra:
            raise AttributeError(
                "Use of this property requires installation of the "
                '"snowflake" extra for analytics-etl:\n'
                "pip3 install 'analytics-etl[snowflake]'"
            )
        if not self.snowflake_connection_string:
            raise AttributeError(
                "You must provide a Snowflake connection string"
            )
        if not self.snowflake_base:
            raise AttributeError(
                "You must provide a Snowflake declarative base"
            )
        if self.echo:
            log.info("Establishing Snowflake connection")
        session: Session = _get_session(
            base=self.snowflake_base,
            connection_string=self.snowflake_connection_string,
            echo=self.echo,
        )
        connection: Connection = session.bind.connect()
        connection.exec_driver_sql("USE SECONDARY ROLES ALL")
        connection.exec_driver_sql("COMMIT")
        return session

    @property  # type: ignore
    @sqlalchemy_session_lru_cache()
    def postgresql_session(self) -> Session:
        """
        This is a SQLAlchemy ORM Session for the Snowflake database
        """
        if not has_postgresql_extra:
            raise AttributeError(
                "Use of this property requires installation of the "
                '"postgresql" extra for analytics-etl:\n'
                "pip3 install 'analytics-etl[postgresql]'"
            )
        if not self.postgresql_connection_string:
            raise AttributeError(
                "You must provide a PostgreSQL connection string"
            )
        if not self.postgresql_base:
            raise AttributeError(
                "You must provide a PostgreSQL declarative base"
            )
        if self.echo:
            log.info("Establishing PostgreSQL connection")
        return _get_session(
            base=self.postgresql_base,
            connection_string=self.postgresql_connection_string,
            echo=self.echo,
        )

    def get_databricks_spark_dataframe(
        self,
        table: str,
        column: Optional[str] = None,
        lower_bound: Union[str, int, None] = None,
        upper_bound: Union[str, int, None] = None,
        num_partitions: Optional[int] = None,
        predicates: Optional[List[str]] = None,
    ) -> SparkDataFrame:
        """
        Get a Spark DataFrame from a (fully qualified) Databricks table name or
        `SELECT` statement.

        Parameters:

        - table (str): A fully-qualified table name, such as
          `CATALOG.SCHEMA.TABLE`,  or a sub-query suitable for use in a FROM
          clause, including the surrounding parenthesis, such as
          `(SELECT * FROM CATALOG.SCHEMA.TABLE)`.
        - column (str|None)
        - lower_bound (str|int|None)
        - upper_bound (str|int|None)
        - num_partitions (int|None))
        - predicates ([str]|None)
        """
        url: URL = self.databricks_session.bind.engine.url
        schema: str = url.query.get("schema", "default")
        item: Tuple[str, Any]
        try:
            return self.spark_session.read.jdbc(
                url=f"jdbc:databricks://{url.host}:{url.port or 443}/{schema}",
                table=table,
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
                **dict(
                    filter(
                        lambda item: item[1] is not None,
                        (
                            ("column", column),
                            ("lowerBound", lower_bound),
                            ("upperBound", upper_bound),
                            ("numPartitions", num_partitions),
                            ("predicates", predicates),
                        ),
                    )
                ),
            )
        except Exception as error:
            append_exception_text(
                error, f"Error retrieving Snowflake data frame: {table}"
            )
            raise error

    def get_snowflake_spark_dataframe(
        self,
        table: str,
        column: Optional[str] = None,
        lower_bound: Union[str, int, None] = None,
        upper_bound: Union[str, int, None] = None,
        num_partitions: Optional[int] = None,
        predicates: Optional[List[str]] = None,
    ) -> SparkDataFrame:
        """
        Get a Spark DataFrame from a (fully qualified) Snowflake table name or
        `SELECT` statement.

        Parameters:

        - table (str): A fully-qualified table name, such as
          `DATABASE.SCHEMA.TABLE`,  or a sub-query suitable for use in a FROM
          clause, including the surrounding parenthesis, such as
          `(SELECT * FROM DATABASE.SCHEMA.TABLE)`.
        - column (str|None)
        - lower_bound (str|int|None)
        - upper_bound (str|int|None)
        - num_partitions (int|None))
        - predicates ([str]|None)
        """
        # Get our credentials from the Snowflake SQLAlchemy ORM session
        url: URL = self.snowflake_session.bind.engine.url
        item: Tuple[str, Any]
        try:
            return self.spark_session.read.jdbc(
                url=f"jdbc:snowflake://{url.host}.snowflakecomputing.com",
                table=table,
                properties=dict(
                    database=(
                        url.database.partition("/")[0]
                        if url.database
                        else None
                    ),
                    user=url.username,
                    role="ALL",
                    warehouse=url.query["warehouse"],
                    authenticator=url.query["authenticator"],
                    **(
                        {}
                        if url.query["authenticator"] == "externalbrowser"
                        else {
                            "password": url.password,
                        }
                    ),
                ),
                **dict(
                    filter(
                        lambda item: item[1] is not None,
                        (
                            ("column", column),
                            ("lowerBound", lower_bound),
                            ("upperBound", upper_bound),
                            ("numPartitions", num_partitions),
                            ("predicates", predicates),
                        ),
                    )
                ),
            )
        except Exception as error:
            append_exception_text(
                error, f"Error retrieving Snowflake data frame: {table}"
            )
            raise error

    def _spark_read_parquet_url_pattern(
        self, url_pattern: str, schema: StructType
    ) -> SparkDataFrame:
        log.info(f"Reading from {url_pattern}")
        try:
            # First attempt without imposing a schema
            return self.spark_session.read.parquet(url_pattern)
        except AnalysisException as error:
            if not is_spark_path_not_found_error(error):
                try:
                    # Attempt using the schema
                    return self.spark_session.read.parquet(
                        url_pattern, schema=schema  # type: ignore
                    )
                except AnalysisException as error:
                    if not is_spark_path_not_found_error(error):
                        raise
        return self.spark_session.createDataFrame((), schema=schema)

    def get_delta_table(
        self, table_name: str, schema: Optional[StructType] = None
    ) -> DeltaTable:
        """
        Get a Spark DataFrame for a delta lake table

        Parameters:

        - table_name (str)
        """
        if self._is_databricks():
            bind_url_query: Dict[str, str] = (
                self.databricks_session.bind.engine.url.query
            )
            return DeltaTable.forName(
                self.spark_session,
                f"{bind_url_query['catalog']}."
                f"{bind_url_query['schema']}."
                f"{table_name.lower()}",
            )
        file_system: FileSystem = cast(FileSystem, self.file_system)
        path: str = f"{self.tables_directory}{table_name}/"
        url: str = file_system.get_url(path)
        log.info(f"Retrieving Delta Table {table_name} from {url}")
        builder: DeltaTableBuilder = (
            DeltaTable.createIfNotExists(self.spark_session)
            .tableName(table_name)
            .location(url)
        )
        if not file_system.is_directory(path):
            if schema is None:
                base: Type[Base] = cast(
                    Type[Base], self.databricks_base or self.snowflake_base
                )
                schema = get_struct_type_from_mapping(
                    get_base_table_name_subclass(base, table_name)
                )
            builder.addColumns(schema)
        return builder.execute()

    def get_table_spark_dataframe(
        self,
        table_name: str,
        schema: Optional[StructType] = None,
    ) -> SparkDataFrame:
        """
        Get a Spark DataFrame for a delta lake or parquet table

        Parameters:

        - table_name (str)
        """
        if self._is_databricks():
            return self.get_delta_table(table_name, schema).toDF()
        elif has_databricks_extra and not isinstance(self.file_system, Local):
            # This job can connect to a Databricks warehouse, but is not
            # running on a Databricks cluster, and is not running local unit
            # tests
            return self.get_databricks_spark_dataframe(table_name.lower())
        else:
            # This job is running local unit tests or cannot connect to
            # a databricks warehouse
            return self.get_delta_table(table_name, schema).toDF()

    @retry(
        errors=(RuntimeError,),
        retry_hook=_write_parquet_retry_hook,
        number_of_attempts=3,
    )
    def write_parquet(
        self,
        rows: Union[DataFrame, Iterable[Tuple[Any, ...]]],
        path: str,
        column_names: Tuple[str, ...] = (),
        schema: Optional[pyarrow.Schema] = None,
    ) -> None:
        """
        Write a parquet file from a pandas DataFrame or an iterable
        of tuples.

        Parameters:

        - rows
        - path (str): A (relative) path wherein to put the parquet file
        - column_names ((str,)) = ()
        - schema (pyarrow.Schema) = None
        """
        assert self.file_system
        message: str
        data_frame: DataFrame
        if isinstance(rows, DataFrame):
            data_frame = rows
        else:
            rows = list(rows)
            # If an empty iterable was provided, there is nothing to write
            if not rows:
                return
            assert column_names, "Column names are required"
            try:
                data_frame = DataFrame(rows, columns=column_names)
            except Exception:
                message = (
                    "Error encountered while attempting to create data frame "
                    '"{}" with columns {}:\n- {}\n\n{}'.format(
                        path,
                        repr(column_names),
                        "\n".join(repr(row) for row in rows),
                        get_exception_text(),
                    )
                )
                log.error(message)
                raise
        with BytesIO() as data_frame_io:
            try:
                data_frame.to_parquet(
                    data_frame_io,  # noqa
                    engine="pyarrow",
                    schema=schema,
                    coerce_timestamps="ms",
                    flavor="spark",
                    allow_truncated_timestamps=True,
                )
            except Exception:
                message = (
                    "Error encountered while attempting to write table "
                    '"{}" with columns {}:\n{}\n\n{}'.format(
                        path,
                        repr(column_names),
                        "\n".join(
                            repr(row) for row in itertools.islice(rows, 100)
                        ),
                        get_exception_text()[-999:],
                    )
                )
                log.error(message)
                raise
            self.file_system.put(data_frame_io, path)

    @lru_cache()
    def _get_column_names(self, qualified_table_name: str) -> Tuple[str, ...]:
        """
        Get a table's column names, in the order they appear in the database.
        """
        query: str = f"show columns in table {qualified_table_name}"
        row: Row
        return tuple(
            row.column_name.upper()
            for row in self.snowflake_session.execute(text(query))
        )

    def get_table_stage_select_statement(self, table_name: str) -> str:
        """
        This method returns a select statement which will retrieve the
        specified table from S3 in a format which can be ingested by
        Snowflake.
        """
        base: Type[Base] = cast(
            Type[Base], self.databricks_base or self.snowflake_base
        )
        cls: Type[Base] = get_base_table_name_subclass(base, table_name)
        qualified_table_name: str = get_class_qualified_table_name(cls)
        return self._get_table_stage_select_statement(
            cls, table_name, qualified_table_name
        )

    def _get_table_stage_select_statement(
        self, cls: Type[Base], table_name: str, qualified_table_name: str
    ) -> str:
        column_names: Tuple[str, ...] = self._get_column_names(
            qualified_table_name
        )
        clauses: List[str] = []

        def _get_column_sort_key(item: Tuple[str, Column]) -> int:
            item_name: str = item[1].name.upper()
            try:
                return column_names.index(item_name)
            except ValueError:
                raise ValueError(
                    "{} not found in {}\n{}".format(
                        repr(item_name),
                        repr(column_names),
                        "".join(format_exception(*sys.exc_info())),
                    )
                )

        property_name: str
        column: Column
        # The columns must be sorted to account for scenarios where the order
        # of the columns in the database does not match the order in which
        # they occur in the ORM
        for property_name, column in sorted(
            get_class_mapper(cls).columns.items(),  # type: ignore
            key=_get_column_sort_key,
        ):
            type_: TypeEngine = _get_sql_type_instance(column.type)
            clause: str = f"$1:{column.name}"
            if isinstance(type_, DateTime):
                clause = f"to_timestamp({clause}::varchar)"
            clauses.append(clause)
        if not self.snowflake_s3_stage_name:
            raise AttributeError("You must provide an S3 stage name")
        return "select {} from @{}/{}{}/".format(
            ", ".join(clauses),
            self.snowflake_s3_stage_name,
            self.tables_directory,
            table_name,
        )

    def snowflake_load_table(self, table_name: str) -> None:
        """
        This method populates a Snowflake table from parquet files in NGAP.

        Parameter:

            - table_name (str): The schema-qualified name of the table
              ("SCHEMA_NAME.TABLE_NAME").
        """
        # Important: `self.snowflake_session` must be accessed before
        # accessing `Base`
        assert self.snowflake_base is not None
        snowflake_session: Session = self.snowflake_session
        self.snowflake_base.metadata.bind = snowflake_session.bind
        log.info(f"Loading {table_name} into Snowflake")
        cls: Type[Base] = get_base_table_name_subclass(
            self.snowflake_base, table_name
        )
        qualified_table_name: str = get_class_qualified_table_name(
            cls, "snowflake"
        )
        table_name = get_class_table_name(cls, "snowflake")
        select_from_stage: str = self._get_table_stage_select_statement(
            cls, table_name, qualified_table_name
        )
        snowflake_session.execute(
            text(f"TRUNCATE TABLE {qualified_table_name}")
        )
        snowflake_session.flush()
        command: str = (
            f"copy into {qualified_table_name} "
            f"from ({select_from_stage}) "
            "pattern='.*.parquet' "
        )
        log.info(command)
        row: Row
        for row in snowflake_session.execute(text(command)):
            log.info(repr(row))
        log.info(f"Finished populating table: {qualified_table_name}")

    def snowflake_copy_into_location(
        self,
        select_statement: Union[Select, str, TextClause],
        location: str,
        column_names: Sequence[str] = (),
        format: str = "TSV",
    ) -> None:
        """
        Copy the results of a SQL `SELECT` statement from Snowflake
        to a specified `location`. See:
        https://docs.snowflake.com/en/sql-reference/sql/copy-into-location.html

        Parameters:

        - select_statement (
            str |
            sqlalchemy.sql.expression.Select |
            sqlalchemy.sql.expression.TextClause
          )
        - location (str): Target path (including @STAGE.NAME if applicable)
        - column_names ([str]): The column names, in the order in which
          they should appear. If not provided, they will appear in the same
          order as the query returns them
        - format ("TSV" | "CSV" | "PARQUET"): The format of the output.
          Note: TSV/CSV will be compressed with GZIP, PARQUET will be
          compressed with SNAPPY.
        """
        preparer: IdentifierPreparer
        dialect: Dialect
        compression: str
        additional_file_format_arguments: str = ""
        format = format.upper()
        assert format in ("TSV", "CSV", "PARQUET")
        if format == "TSV":
            additional_file_format_arguments = ", FIELD_DELIMITER = '\t'"
            format = "CSV"
        if format == "CSV":
            compression = "GZIP"
            additional_file_format_arguments = (
                f"{additional_file_format_arguments}"
                ", EMPTY_FIELD_AS_NULL = FALSE"
                ", NULL_IF = ''"
            )
        else:
            compression = "SNAPPY"
        dialect = self.snowflake_session.bind.engine.dialect
        if isinstance(select_statement, Select):
            select_statement = select_statement.compile(
                compile_kwargs={"literal_binds": True},
                dialect=dialect,
                bind=self.snowflake_session.bind,
            )
        elif isinstance(select_statement, TextClause):
            select_statement = str(select_statement)
        if column_names:
            preparer = getattr(dialect, "preparer")(dialect)
            quoted_column_names: str = ", ".join(
                map(preparer.quote, column_names)
            )
            select_statement = (
                f"SELECT {quoted_column_names} FROM ({select_statement})"
            )
        copy_into_statement: str = (
            f"COPY INTO {location} "
            f"FROM ({select_statement}) "
            "INCLUDE_QUERY_ID = TRUE "
            "FILE_FORMAT = ("
            f"TYPE = '{format}', "
            f"COMPRESSION = '{compression}'"
            f"{additional_file_format_arguments}"
            ") INCLUDE_QUERY_ID = TRUE"
        )
        connection: Connection = self.snowflake_session.bind.connect()
        connection.exec_driver_sql("USE SECONDARY ROLES ALL")
        connection.exec_driver_sql("COMMIT")
        rows: Iterable[Row]
        try:
            rows = connection.exec_driver_sql(copy_into_statement)
        except Exception as error:
            # Include the current roles in the error message
            role: str = next(
                iter(connection.exec_driver_sql("SELECT CURRENT_ROLE()"))
            )[0]
            secondary_roles: str = json.loads(
                next(
                    iter(
                        connection.exec_driver_sql(
                            "SELECT CURRENT_SECONDARY_ROLES()"
                        )
                    )
                )[0]
            )["roles"]
            append_exception_text(
                error,
                (
                    f"\nCurrent Role: {role}"
                    f"\nCurrent Secondary Roles: {secondary_roles}\n"
                ),
            )
            raise error
        # Execute the statement and log the response
        row: Row
        for row in rows:
            repr_row: str = repr(row)
            if repr_row.strip("{}() "):
                log.info(repr_row)
        self.snowflake_session.commit()


def default_snowflake_load_filter_function(qualified_table_name: str) -> bool:
    return not (
        qualified_table_name.startswith("BCL_")
        or qualified_table_name.endswith("_MV")
        or qualified_table_name.endswith("_V")
        or qualified_table_name.partition("_MV_")[-1]
        or qualified_table_name.partition("_V_")[-1]
    )


_CLUSTER_NAME_JOB_RUN_PATTERN: Pattern = re.compile(
    r"job-(?P<job_id>\d+)-run-(?P<run_id>\d+)(?:-(?P<job_name>.+))?"
)


class Broker:
    """
    Instances of this class, or more typically sub-classes of this class,
    broker exchanges of data between systems and distribute tasks to instances
    of `Work` or a `Work` sub-class.

    Parameters:

    - parallelism (int) = None: If this is 0 or `None`, the default
      parallelism for the Spark cluster will be used.
    - concurrency (analytics_etl.concurrency.Concurrency)
      = analytics_etl.concurrency.Concurrency.MULTIPROCESSING
    - file_system (file_system_client.base.FileSystem)
    - databricks_base (typing.Type[analytics_orm.declarative.Base]|None)
    - snowflake_base (typing.Type[analytics_orm.declarative.Base]|None)
    - postgresql_base (typing.Type[analytics_orm.declarative.Base]|None)
    - postgresql_connection_string (str)
    - snowflake_connection_string (str)
    - databricks_connection_string (str)
      for writing dataframes to s3, in lieu of the file system root
    - started (datetime.datetime|None):
      The date and time at which the job started, for bookmarking purposes.
    - echo (bool)
    - consolidate_dont_raise_exceptions ((Exception, ...)) = ():
      A tuple of exceptions which should not be raised by the `consolidate`
      method, only logged. This should only be used for known local testing
      scenarios.
    """

    work: Work

    def __init__(
        self,
        file_system: Union[FileSystem, str],
        parallelism: Optional[int] = None,
        concurrency: Concurrency = Concurrency.MULTIPROCESSING,
        databricks_base: Optional[Type[Base]] = None,
        snowflake_base: Optional[Type[Base]] = None,
        postgresql_base: Optional[Type[Base]] = None,
        postgresql_connection_string: str = "",
        snowflake_connection_string: str = "",
        databricks_connection_string: str = "",
        tables_directory: str = "tables/",
        temp_directory: str = "temp/",
        snowflake_s3_stage_name: str = "",
        started: Optional[datetime] = None,
        echo: bool = False,
        work: Union[Work, Type[Work]] = Work,
        consolidate_dont_raise_exceptions: Tuple[Type[Exception], ...] = (),
    ) -> None:
        log.info(
            "$ pip freeze --all\n{}".format(
                check_output(
                    (sys.executable, "-m", "pip", "freeze", "--all"), text=True
                )
            )
        )
        if isinstance(file_system, str):
            file_system = from_url(file_system)
        assert (file_system is None) or isinstance(
            file_system, FileSystem
        ), repr(file_system)
        assert isinstance(echo, bool)
        assert (parallelism is None) or isinstance(parallelism, int)
        self.parallelism: Optional[int] = parallelism or None
        self.concurrency: Concurrency = concurrency
        self.consolidate_dont_raise_exceptions: Tuple[Type[Exception], ...] = (
            consolidate_dont_raise_exceptions
        )
        if isinstance(work, type):
            assert issubclass(work, Work)
            work = work(
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
        else:
            assert isinstance(work, Work)
            if started:
                work.started = started
        self.work: Work = work
        if echo:
            get_print_logger(s3.log.name)
        # This ensures the spark session is initiated, even if not used,
        # so that Spark Jobs don't return an error erroneously for
        # tasks which execute only on the driver
        if concurrency == Concurrency.SPARK:
            assert self.work.spark_session
        # To validate PYPI library versions, we need the databricks
        # extra, in addition to spark, because we infer API connection
        # information from the databricks SQLAlchemy session URL
        if has_databricks_extra and self.work._is_databricks():
            self.work._validate_databricks_pypi_library_versions()

    def get_effective_parallelism_concurrency(
        self,
        parallelism: Optional[int] = None,
        concurrency: Optional[Concurrency] = None,
    ) -> Tuple[int, Concurrency]:
        """
        Get the effective parallelism and concurrency for the provided
        parameter values.

        Parameters:

        - parallelism (int) = None
        - concurrency (analytics_etl.concurrency.Concurrency) = None
        """
        effective_parallelism: int = (
            parallelism or self.parallelism  # type: ignore
        )
        effective_concurrency: Concurrency = concurrency or self.concurrency
        if effective_parallelism is None:
            if effective_concurrency == Concurrency.SPARK:
                effective_parallelism = (
                    self.work.spark_session.sparkContext.defaultParallelism
                )
            elif effective_concurrency in (
                Concurrency.MULTIPROCESSING,
                Concurrency.FUTURES,
            ):
                effective_parallelism = os.cpu_count()
            else:
                effective_parallelism = 1
        return effective_parallelism, effective_concurrency

    def map(
        self,
        function: Callable,
        arguments: Iterable[Any],
        concurrency: Optional[Concurrency] = None,
        parallelism: Optional[int] = None,
        pre_partition: bool = True,
    ) -> List[Any]:
        """
        This method will map a function which accepts one argument to an
        iterable, either for sequential or parallel execution.
        """
        if not concurrency:
            concurrency = self.concurrency
        if concurrency == Concurrency.NONE:
            return list(map(function, arguments))
        elif concurrency == Concurrency.SPARK:
            rdd: RDD = self.work.spark_session.sparkContext.parallelize(
                arguments, parallelism or self.parallelism
            )
            if pre_partition:
                rdd = rdd.mapPartitions(_map_partitions_wrap(function))
            else:
                rdd = rdd.map(function)
            return rdd.collect()
        elif concurrency == Concurrency.FUTURES:
            return list(
                ProcessPoolExecutor(
                    max_workers=parallelism or self.parallelism
                ).map(function, arguments)
            )
        else:
            assert concurrency == Concurrency.MULTIPROCESSING
            return Pool(processes=parallelism or self.parallelism).map(
                function, arguments
            )

    def starmap(
        self,
        function: Callable,
        arguments: Iterable[Sequence],
        concurrency: Optional[Concurrency] = None,
        parallelism: Optional[int] = None,
        pre_partition: bool = True,
    ) -> List[Any]:
        """
        This method will map a function which accepts multiple arguments to an
        iterable, either for sequential or parallel execution.
        """
        if not concurrency:
            concurrency = self.concurrency
        if concurrency == Concurrency.NONE:
            return list(starmap(function, arguments))
        elif concurrency == Concurrency.SPARK:
            rdd: RDD = self.work.spark_session.sparkContext.parallelize(
                arguments, parallelism or self.parallelism
            )
            if pre_partition:
                rdd = rdd.mapPartitions(_star_map_partitions_wrap(function))
            else:
                rdd = rdd.map(_star_map_wrap(function))
            return rdd.collect()
        elif concurrency == Concurrency.FUTURES:
            return list(
                ProcessPoolExecutor(
                    max_workers=parallelism or self.parallelism
                ).map(_star_map_wrap(function), arguments)
            )
        else:
            assert concurrency == Concurrency.MULTIPROCESSING
            return Pool(processes=parallelism or self.parallelism).starmap(
                function, arguments
            )

    def consolidate(
        self,
        source_directory: str,
        target_directory: str = "",
        pre_existing_data_frame_hook: Union[
            # A function which receives only the pre-existing, "target" data
            # frame (spark or pandas), and an ORM table class
            Callable[[DataFrame, type], DataFrame],
            Callable[[SparkDataFrame, type], SparkDataFrame],
            # A function which receives both a source data frame *and*
            # a pre-existing, "target" data frame (spark or pandas), and an
            # ORM table class
            Callable[[DataFrame, DataFrame, type], DataFrame],
            Callable[[SparkDataFrame, SparkDataFrame, type], SparkDataFrame],
            None,
        ] = None,
        concurrency: Optional[Concurrency] = None,
        parallelism: Optional[int] = None,
        overwrite: bool = True,
        defaults: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Read parquet files with repeating primary keys and write parquet
        files with non-repeating primary keys, for all sub-directories of the
        most recently timestamped sub-directory of `source_directory`.

        Parameters:

        - source_directory (str)
        - target_directory (str) = "": If not provided, this will be
          the semantic directory (where hive tables are stored)
        - pre_existing_data_frame_hook = None: If provided, this function
          will be applied to a data frame of the pre-existing (target) data,
          and will transform that pre-existing data before the new
          data is merged into it.
        - concurrency (analytics_etl.concurrency.Concurrency) = None:
          If not provided, this will default to the class'es concurrency
          type
        - parallelism (int) = None
        - overwrite (bool) = True
        - defaults ({str: typing.Any}|None) = None: A mapping of column
          names to default values to fill in when/if adding columns.
        """
        assert self.work.file_system
        effective_concurrency: Concurrency
        effective_parallelism: int
        (
            effective_parallelism,
            effective_concurrency,
        ) = self.get_effective_parallelism_concurrency(
            concurrency=concurrency, parallelism=parallelism
        )
        source_directory = f"{source_directory.rstrip('/ ')}/"
        if target_directory:
            target_directory = f"{target_directory.rstrip('/ ')}/"
        log.info(
            f"{self.__module__}.{self.__class__.__name__}"
            "().consolidate("
            f"source_directory={repr(source_directory)}, "
            f"target_directory={repr(target_directory)}, "
            f"parallelism={repr(effective_parallelism)}, "
            "concurrency="
            f"{Concurrency.__module__}.{str(effective_concurrency)}"
            ")"
        )
        latest_source_directory: str
        latest_source_sub_directories: Iterable[str]
        if is_date_partition_directory(source_directory):
            # If the provided source directory *is* the latest directory
            # and not a parent directory, we just need to get its
            # direct sub-directories
            latest_source_directory = source_directory
            latest_source_sub_directories = (
                self.work.file_system.iter_sub_directories(source_directory)
            )
        else:
            (
                latest_source_directory,
                latest_source_sub_directories,
            ) = self.work.file_system.iter_latest_directory_sub_directories(
                source_directory
            )
            if not latest_source_directory:
                raise FileNotFoundError(
                    "Could not find a latest source directory in "
                    "{}:\n- {}".format(
                        self.work.file_system.get_absolute_path(
                            source_directory
                        ),
                        "\n- ".join(
                            self.work.file_system.iter_file_paths(
                                source_directory
                            )
                        ),
                    )
                )
        log.info(
            "Consolidating:\n"
            f"- Source Directory: {latest_source_directory}\n"
            f"- Target Directory: {target_directory}"
        )
        latest_source_sub_directory: str
        for latest_source_sub_directory in latest_source_sub_directories:
            table_name: str = latest_source_sub_directory.rstrip("/ ").split(
                "/"
            )[-1]
            target_sub_directory: str = (
                f"{target_directory}{table_name}/" if target_directory else ""
            )
            log.info(
                f"Consolidating {latest_source_sub_directory} -> "
                f"{target_sub_directory}"
            )
            try:
                self.consolidate_table(
                    source_directory=latest_source_sub_directory,
                    target_directory=target_sub_directory,
                    table_name=table_name,
                    pre_existing_data_frame_hook=pre_existing_data_frame_hook,
                    concurrency=concurrency,
                    parallelism=parallelism,
                    overwrite=overwrite,
                    defaults=defaults,
                )
            except Exception as error:
                if type(error) in self.consolidate_dont_raise_exceptions:
                    log.info(
                        "Failed to consolidate: "
                        f"{latest_source_sub_directory}\n"
                        f"{get_exception_text()}"
                    )
                else:
                    raise

    def consolidate_table(
        self,
        source_directory: str,
        target_directory: str = "",
        table_name: str = "",
        pre_existing_data_frame_hook: Union[
            # A function which receives only the pre-existing, "target" data
            # frame (spark or pandas), and an ORM table class
            Callable[[DataFrame, type], DataFrame],
            Callable[[SparkDataFrame, type], SparkDataFrame],
            # A function which receives both a source data frame *and*
            # a pre-existing, "target" data frame (spark or pandas), and an
            # ORM table class
            Callable[[DataFrame, DataFrame, type], DataFrame],
            Callable[[SparkDataFrame, SparkDataFrame, type], SparkDataFrame],
            None,
        ] = None,
        overwrite: Optional[bool] = False,
        defaults: Optional[Dict[str, Any]] = None,
        concurrency: Optional[Concurrency] = None,
        parallelism: Optional[int] = None,
    ) -> str:
        """
        Read parquet files with repeating primary keys and write parquet
        files with non-repeating primary keys.

        Parameters:

        - source_directory (str)
        - target_directory (str) = "": If left empty, this will be inferred
          from the `table_name`.
        - table_name (str) = "": If left empty, this will be inferred from
          the lowest-level source sub-directory
        - pre_existing_data_frame_hook = None: If provided, this function
          will be applied to a data frame of the pre-existing (target) data,
          and will transform that pre-existing data before the new
          data is merged into it.
        - concurrency (analytics_etl.concurrency.Concurrency) = None:
          If not provided, this will default to the class'es concurrency
          type
        - parallelism (int) = None
        - defaults ({str: typing.Any}|None) = None: A mapping of column
          names to default values to fill in when/if adding columns.
        """
        effective_concurrency: Concurrency
        effective_parallelism: int
        (
            effective_parallelism,
            effective_concurrency,
        ) = self.get_effective_parallelism_concurrency(
            concurrency=concurrency, parallelism=parallelism
        )
        log.info(
            f"{self.__module__}.{self.__class__.__name__}"
            "().consolidate_table("
            f"source_directory={repr(source_directory)}, "
            f"target_directory={repr(target_directory)}, "
            f"table_name={repr(table_name)}, "
            f"parallelism={repr(effective_parallelism)}, "
            "concurrency="
            f"{Concurrency.__module__}.{str(effective_concurrency)}"
            ")"
        )
        if effective_concurrency == Concurrency.SPARK:
            return self._spark_consolidate_table(
                source_directory,
                target_directory,
                table_name,
                cast(
                    Union[
                        Callable[[SparkDataFrame, type], SparkDataFrame],
                        Callable[
                            [SparkDataFrame, SparkDataFrame, type],
                            SparkDataFrame,
                        ],
                        None,
                    ],
                    pre_existing_data_frame_hook,
                ),
                overwrite=overwrite,
                defaults=defaults,
            )
        else:
            return self._pandas_consolidate_table(
                source_directory,
                target_directory,
                table_name,
                cast(
                    Union[
                        Callable[[DataFrame, type], DataFrame],
                        Callable[[DataFrame, DataFrame, type], DataFrame],
                        None,
                    ],
                    pre_existing_data_frame_hook,
                ),
                parallelism=parallelism,
                concurrency=concurrency,
                overwrite=overwrite,
                defaults=defaults,
            )

    def _pandas_consolidate_table(
        self,
        source_directory: str,
        target_directory: str = "",
        table_name: str = "",
        pre_existing_data_frame_hook: Union[
            # A function which receives only the pre-existing, "target" data
            # frame (spark or pandas), and an ORM table class
            Callable[[DataFrame, type], DataFrame],
            # A function which receives both a source data frame *and*
            # a pre-existing, "target" data frame (spark or pandas), and an
            # ORM table class
            Callable[[DataFrame, DataFrame, type], DataFrame],
            None,
        ] = None,
        overwrite: Optional[bool] = False,
        defaults: Optional[Dict[str, Any]] = None,
        concurrency: Optional[Concurrency] = None,
        parallelism: Optional[int] = None,
    ) -> str:
        raise NotImplementedError()

    def _spark_consolidate_table(
        self,
        source_directory: str,
        target_directory: str = "",
        table_name: str = "",
        pre_existing_data_frame_hook: Union[
            # A function which receives only the pre-existing, "target" data
            # frame (spark or pandas), and an ORM table class
            Callable[[SparkDataFrame, type], SparkDataFrame],
            # A function which receives both a source data frame *and*
            # a pre-existing, "target" data frame (spark or pandas), and an
            # ORM table class
            Callable[[SparkDataFrame, SparkDataFrame, type], SparkDataFrame],
            None,
        ] = None,
        overwrite: Optional[bool] = False,
        defaults: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Read from parquet files in the source directory, consolidate records
        by primary key, then merge that data with an existing S3 parquet
        "table".

        Parameters:

        - source_directory (str)
        - target_directory (str) = "": If not provided, this will be inferred
          from the table name or source directory name.
        - table_name (str) = "": If not provided, this will be inferred from
          the target directory name or source directory name.
        - pre_existing_data_frame_hook = None: If provided, this function
          will be applied to a data frame of the pre-existing (target) data,
          and will transform that pre-existing data before the new
          data is merged into it.
        - overwrite (bool) = False: If `True` overwrite pre-existing data,
          otherwise merge/upsert with pre-existing data.
        """
        if overwrite is None:
            overwrite = False
        if not source_directory.endswith("/"):
            source_directory = f"{source_directory}/"
        assert self.work.file_system
        source_url_pattern: str = self.work.file_system.get_url(
            source_directory
        )
        # Infer a table name if needed
        if not table_name:
            if target_directory:
                table_name = target_directory.rstrip("/ ").split("/")[-1]
            else:
                table_name = source_directory.rstrip("/ ").split("/")[-1]
        log.info(f"Reading from {source_url_pattern}")
        # Read parquet files contributing to the table into a data frame
        base: Type[Base] = cast(
            Type[Base], self.work.databricks_base or self.work.snowflake_base
        )
        table_class: Type[Base] = get_base_table_name_subclass(
            base, table_name
        )
        source_data_frame: SparkDataFrame = (
            get_data_frame_with_unique_primary_keys(
                self.work.spark_session.read.parquet(
                    source_url_pattern,
                    schema=get_struct_type_from_mapping(  # type: ignore
                        get_base_table_name_subclass(base, table_name)
                    ),
                ),
                table_class,
            )
        )
        log.info(
            f"Consolidating {table_name}:\n"
            f"{source_directory} -> {target_directory}"
        )
        return self._spark_merge(
            source_data_frame,
            table_name,
            target_directory,
            pre_existing_data_frame_hook,
            defaults=defaults,
            overwrite=overwrite,
        )

    def _spark_merge(  # noqa: C901
        self,
        data_frame: SparkDataFrame,
        table_name: str = "",
        directory: str = "",
        pre_existing_data_frame_hook: Union[
            # A function which receives only the pre-existing, "target" data
            # frame (spark or pandas), and an ORM table class
            Callable[[SparkDataFrame, type], SparkDataFrame],
            # A function which receives both a source data frame *and*
            # a pre-existing, "target" data frame (spark or pandas), and an
            # ORM table class
            Callable[[SparkDataFrame, SparkDataFrame, type], SparkDataFrame],
            None,
        ] = None,
        defaults: Optional[Dict[str, Any]] = None,
        overwrite: bool = False,
    ) -> str:
        """
        Merge a Spark data frame into a databricks table, or a parquet table
        if working with a local file system.

        Parameters:

        - data_frame (pyspark.sql.DataFrame)
        - table_name (str) = "": If not provided, this will be inferred from
          the target directory name.
        - directory (str) = "": If not provided, this will be inferred
          from the table name.
        - pre_existing_data_frame_hook = None: If provided, this function
          will be applied to a data frame of the pre-existing (target) data,
          and will transform that pre-existing data before the new
          data is merged into it.
        - defaults ({str: typing.Any}|None) = None: A mapping of column
          names to default values to fill in when/if adding columns.
        """
        # If a directory is explicitly specified, we don't merge into a delta
        # table, we just write parquet files
        parquet_files_only: bool = True if directory else False
        # Infer a table name if needed
        if not table_name:
            table_name = directory.rstrip("/ ").split("/")[-1]
        if not directory:
            directory = f"{self.work.tables_directory}{table_name}/"
        assert self.work.file_system
        target_url: str = self.work.file_system.get_url(directory)
        temp_directory: str = f"{self.work.temp_directory}{table_name}/"
        temp_url: str = self.work.file_system.get_url(temp_directory)
        base: Type[Base] = cast(
            Type[Base], self.work.databricks_base or self.work.snowflake_base
        )
        schema: StructType = get_struct_type_from_mapping(
            get_base_table_name_subclass(base, table_name)
        )
        table_class: Type[Base] = get_base_table_name_subclass(
            base, table_name
        )
        #######################################################################
        # TODO: Delete the following (and related logic) after all jobs have
        # been upgraded and run at least once (all delta tables are populated)
        #######################################################################
        # Check if the target delta table is empty, and use the corresponding
        # parquet files if it is.
        target_delta_table_is_empty: bool = False
        if (not parquet_files_only) and self.work._is_databricks():
            target_delta_table_is_empty = (
                False
                if self.work.get_table_spark_dataframe(
                    table_name, schema
                ).count()
                else True
            )
        #######################################################################
        if (
            ((pre_existing_data_frame_hook is not None) and not overwrite)
            or parquet_files_only
            or target_delta_table_is_empty
        ):
            target_data_frame: SparkDataFrame = (
                self.work._spark_read_parquet_url_pattern(target_url, schema)
                if parquet_files_only or target_delta_table_is_empty
                else self.work.get_table_spark_dataframe(table_name, schema)
            )
            if (pre_existing_data_frame_hook is not None) and not overwrite:
                # Make sure we were provided with a function
                assert callable(pre_existing_data_frame_hook)
                # Determine how many parameters the function requires,
                # so that we can pass the correct number of arguments
                parameter_count: int = len(
                    inspect.signature(
                        pre_existing_data_frame_hook
                    ).parameters.keys()
                )
                if parameter_count == 2:
                    target_data_frame = pre_existing_data_frame_hook(
                        target_data_frame, table_class  # type: ignore
                    )
                elif parameter_count == 3:
                    target_data_frame = pre_existing_data_frame_hook(
                        data_frame,
                        target_data_frame,  # type: ignore
                        table_class,
                    )
                else:
                    raise ValueError(
                        "Your `pre_existing_data_frame_hook` requires an "
                        f"unsupported number of arguments: {parameter_count}"
                    )
            if not overwrite:
                # Merge and de-duplicate records
                data_frame = merge_data_frames(
                    (data_frame, target_data_frame),
                    table_class,
                    defaults=defaults,
                )
            # if we've merged with the target data, we need to use
            # temporary storage prior to our merge
            log.info(f"Writing to {temp_url}")
            data_frame.write.parquet(temp_url, mode="overwrite")
            data_frame = self.work.spark_session.read.parquet(
                temp_url, schema=schema  # type: ignore
            )
        if parquet_files_only:
            log.info(f"Writing to {target_url}")
            data_frame.write.parquet(target_url, mode="overwrite")
        else:
            # Write to the delta tables
            log.info(f"Writing {table_name}")
            alias: str = f"new_{table_name}"
            merge_builder: DeltaMergeBuilder = (
                self.work.get_delta_table(table_name, schema)
                .merge(  # type: ignore
                    data_frame.alias(alias),
                    condition=" and ".join(
                        f"{table_name}.{column_name} = "
                        f"{alias}.{column_name}"
                        for column_name in get_class_primary_key_column_names(
                            table_class
                        )
                    ),
                )
                .whenMatchedUpdateAll()
                .whenNotMatchedInsertAll()
            )
            if overwrite:
                merge_builder = merge_builder.whenNotMatchedBySourceDelete()
            merge_builder.execute()
            if self.work._is_databricks():
                # Dump the databricks table to parquet files
                self.work.get_table_spark_dataframe(
                    table_name, schema
                ).write.parquet(target_url, mode="overwrite")
        if (
            (pre_existing_data_frame_hook is not None) and not overwrite
        ) or parquet_files_only:
            # Cleanup temporary files
            self.work.file_system.clear(temp_url)
        return target_url

    def _pandas_merge(
        self,
        data_frame: DataFrame,
        table_name: str = "",
        directory: str = "",
        pre_existing_data_frame_hook: Union[
            # A function which receives only the pre-existing, "target" data
            # frame (spark or pandas), and an ORM table class
            Callable[[DataFrame, type], DataFrame],
            # A function which receives both a source data frame *and*
            # a pre-existing, "target" data frame (spark or pandas), and an
            # ORM table class
            Callable[[DataFrame, DataFrame, type], DataFrame],
            None,
        ] = None,
        defaults: Optional[Dict[str, Any]] = None,
        overwrite: bool = False,
    ) -> None:
        """
        Merge a Pandas data frame into an S3 parquet "table".

        Parameters:

        - data_frame (pyspark.sql.DataFrame)
        - target_directory (str) = "": If not provided, this will be inferred
          from the table name.
        - table_name (str) = "": If not provided, this will be inferred from
          the target directory name.
        - pre_existing_data_frame_hook = None: If provided, this function
          will be applied to a data frame of the pre-existing (target) data,
          and will transform that pre-existing data before the new
          data is merged into it.
        - defaults ({str: typing.Any}|None) = None: A mapping of column
          names to default values to fill in when/if adding columns.

        TODO: Implement `Broker._pandas_merge`
        """
        raise NotImplementedError()

    def merge(
        self,
        data: Union[SparkDataFrame, DataFrame, Iterable[Tuple[Any, ...]]],
        table_name: str = "",
        pre_existing_data_frame_hook: Union[
            # A function which receives only the pre-existing, "target" data
            # frame (spark or pandas), and an ORM table class
            Callable[[DataFrame, type], DataFrame],
            Callable[[SparkDataFrame, type], SparkDataFrame],
            # A function which receives both a source data frame *and*
            # a pre-existing, "target" data frame (spark or pandas), and an
            # ORM table class
            Callable[[DataFrame, DataFrame, type], DataFrame],
            Callable[[SparkDataFrame, SparkDataFrame, type], SparkDataFrame],
            None,
        ] = None,
        defaults: Optional[Dict[str, Any]] = None,
        directory: str = "",
        concurrency: Optional[Concurrency] = None,
        overwrite: bool = False,
    ) -> None:
        """
        Merge a Spark data frame into an S3 parquet "table".

        Parameters:

        - data_frame (pyspark.sql.DataFrame|pandas.DataFrame)
        - table_name (str) = "": If not provided, this will be inferred from
          the directory name.
        - directory (str) = "": If not provided, this will be inferred
          from the table name.
        - pre_existing_data_frame_hook = None: If provided, this function
          will be applied to a data frame of the pre-existing (target) data,
          and will transform that pre-existing data before the new
          data is merged into it.
        - defaults ({str: typing.Any}|None) = None: A mapping of column
          names to default values to fill in when/if adding columns.
        - concurrency (analytics_etl.concurrency.Concurrency|None)
          = None: This parameter is only meaningful if the `data` is an
          iterable rather than a data frame.
        """
        if not concurrency:
            concurrency = self.concurrency
        if not isinstance(data, ((SparkDataFrame, DataFrame))):
            if concurrency == Concurrency.SPARK:
                data = list(data)
                # If an empty iterable was provided, there is nothing to write
                if not data:
                    return
                # Infer the table name if needed
                if not table_name:
                    table_name = directory.rstrip("/ ").split("/")[-1]
                # Determine column names from table
                base: Type[Base] = cast(
                    Type[Base],
                    self.work.databricks_base or self.work.snowflake_base,
                )
                data = self.work.spark_session.createDataFrame(
                    data,
                    schema=get_struct_type_from_mapping(
                        get_base_table_name_subclass(base, table_name)
                    ),
                )
            else:
                data = DataFrame(data)
        if isinstance(data, SparkDataFrame):
            self._spark_merge(
                data,
                table_name,
                directory,
                cast(
                    Union[
                        Callable[[SparkDataFrame, type], SparkDataFrame],
                        Callable[
                            [SparkDataFrame, SparkDataFrame, type],
                            SparkDataFrame,
                        ],
                        None,
                    ],
                    pre_existing_data_frame_hook,
                ),
                defaults=defaults,
                overwrite=overwrite,
            )
        else:
            assert isinstance(data, DataFrame)
            self._pandas_merge(
                data,
                table_name,
                directory,
                cast(
                    Union[
                        Callable[[DataFrame, type], DataFrame],
                        Callable[
                            [DataFrame, DataFrame, type],
                            DataFrame,
                        ],
                        None,
                    ],
                    pre_existing_data_frame_hook,
                ),
                defaults=defaults,
                overwrite=overwrite,
            )

    def snowflake_load(
        self,
        filter_function: Callable[
            [str], bool
        ] = default_snowflake_load_filter_function,
    ) -> None:
        """
        This method loads all semantic/aggregated data into Snowflake.

        Parameters:

        - filter_function (typing.Callable) = None: By default, all tables
          are loaded from S3 to Snowflake. If a `filter_function` argument is
          provided—it should accept a schema-qualified table name and return
          a boolean indicating whether or not to load that table.
        """
        assert (
            self.work.snowflake_base and self.work.snowflake_connection_string
        )
        log.info("Loading tables into Snowflake...")
        base: Type[Base] = cast(Type[Base], self.work.snowflake_base)
        deque(
            self.map(
                self.work.snowflake_load_table,
                filter(
                    filter_function,
                    _iter_snowflake_qualified_table_names(base=base),
                ),
                concurrency=Concurrency.NONE,
            ),
            maxlen=0,
        )
        self.work.snowflake_session.commit()
