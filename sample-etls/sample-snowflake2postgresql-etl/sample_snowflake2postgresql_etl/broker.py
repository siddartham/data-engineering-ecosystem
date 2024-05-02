from logging import Logger
import os
import re
import functools
from datetime import datetime
from collections import deque
from itertools import chain
from typing import (
    TYPE_CHECKING,
    Optional,
    Set,
    Type,
    List,
    Callable,
    Dict,
    Any,
    Tuple,
    Iterable,
)
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.sql.expression import text, select  # type: ignore
from sqlalchemy.exc import DBAPIError  # type: ignore
from sqlalchemy.engine import Connection, Engine  # type: ignore
from sqlalchemy.engine.result import Row  # type: ignore
from sqlalchemy.engine.interfaces import Dialect  # type: ignore
from sqlalchemy.sql.compiler import IdentifierPreparer  # type: ignore
from boto3.session import Session as Boto3Session  # type: ignore
from botocore.exceptions import (  # type: ignore
    NoCredentialsError as BotoCoreNoCredentialsError,
    ClientError as BotoCoreClientError,
    HTTPClientError as BotoCoreHTTPClientError,
)
from my_datastore_etl.broker import (
    Broker as _Broker,
    Work as _Work,
)
from analytics_etl.concurrency import Concurrency
from file_system_client.utilities import retry
from file_system_client.s3 import (
    SimpleStorageService,
)
from my_api_datastore_model.base import Base as APIBase
from analytics_orm.declarative import (
    get_base_table_name_subclass,
    get_class_column_names,
    get_class_table_name,
    iter_base_sorted_subclasses,
)
from my_datastore_model.view import (
    get_bind_snowflake_view_select_statement,
)
from my_api_datastore_model.dialects.postgresql import (
    ENVIRONMENTS as POSTGRESQL_ENVIRONMENTS,
    create_environment as create_postgresql_environment,
)
from file_system_client.errors import get_exception_text
from my_datastore_etl.utilities import get_print_logger


API_CSV_DIRECTORY: str = "/api/csv/"
_SNOWFLAKE_QUERIES_DIRECTORY: str = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "_snowflake_queries"
)
STAGE_NAME: str = "STAGE.S3_SUSTAINABILITY"
POSTRGRESQL_AWS_REGION: str = "us-west-2"
POSTGRESQL_DEFAULT_PARAMETER_VALUE: str = ""
POSTGRESQL_DEFAULT_PARAMETER_APPLY_METHOD: str = "pending-reboot"
CICD_ARN_TEST: str = "arn:aws:iam::823498884353:role/NIKE.cicd.tool"
CICD_ARN_PROD: str = "arn:aws:iam::567546912947:role/NIKE.cicd.tool"
ASSUME_ROLE_DURATION_SECONDS: int = 3600
POSTGRESQL_CONNECT_ARGS: Tuple[Tuple[str, str], ...] = (
    (
        "options",
        (
            "-c statement_timeout=3200s "  # 60 Minutes
            "-c lock_timeout=0 "
            "-c tcp_user_timeout=60s "
            "-c wal_sender_timeout=0 "
            "-c idle_in_transaction_session_timeout=600s "  # 10 Minutes
        ),
    ),
)
MAX_PROCESSES: int = 50
work_boto3_session_lru_cache: Callable[
    ...,
    Callable[
        [Callable[["Work"], Boto3Session]], Callable[["Work"], Boto3Session]
    ],
] = functools.lru_cache  # type: ignore
work_str_lru_cache: Callable[
    ..., Callable[[Callable[["Work"], str]], Callable[["Work"], str]]
] = functools.lru_cache  # type: ignore
lru_cache: Any = functools.lru_cache
log: Logger = get_print_logger(__name__)


def _get_aws_role_arn() -> str:
    return os.environ.get("AWS_ROLE_ARN", "")


def _get_assume_role_session_name() -> str:
    return os.environ.get(
        "AWS_ROLE_SESSION_NAME",
        "sample-snowflake2postgresql-etl-{}".format(
            datetime.now()
            .replace(microsecond=0, tzinfo=None)
            .isoformat()
            .replace(":", "-")
            .replace(".", "-")
        )[:64],
    )


def _get_web_identity_token() -> str:
    web_identity_token: str = ""
    web_identity_token_file: str = os.environ.get(
        "AWS_WEB_IDENTITY_TOKEN_FILE", ""
    )
    if web_identity_token_file:
        with open(web_identity_token_file, "r") as web_identity_token_file_io:
            web_identity_token = web_identity_token_file_io.read().strip()
    return web_identity_token


def _get_extract_file_name_query_id(path: str) -> str:
    """
    Parameters:

    - path (str): An S3 object path for a CSV file created by the Snowflake
      `COPY INTO` statement

    Returns: The query ID which produced the file
    """
    file_name: str = path.split("/")[-1]
    if "_" in file_name and "." in file_name:
        return file_name.split("_")[1]
    else:
        return ""


def _is_csv(path: str) -> bool:
    return path.lower().endswith(".csv") or path.lower().endswith(".csv.gz")


class Work(_Work):
    """
    This class encapsulates work to be performed by individual processes in a
    multi-process pool.

    Parameters:

    - environment (str)
    - echo (bool)
    """

    @property  # type: ignore
    @lru_cache()
    def postgresql_arn(self) -> str:
        """
        The ARN to use for connecting to our PostgreSQL AWS account
        """
        # Right now, all PostgreSQL databases are in the prod waffle-iron
        # account
        return CICD_ARN_PROD

    @property  # type: ignore
    @lru_cache()
    def postgresql_db_cluster_identifier(self) -> str:
        """
        The database cluster identifier for this environment
        """
        assert self.environment in POSTGRESQL_ENVIRONMENTS
        environment: str = self.environment
        # Our QA and DEV databases are on the same cluster
        if environment == "qa":
            environment = "dev"
        return f"sustainability-psdata-{environment}"

    @retry((PermissionError,), number_of_attempts=3)
    def _describe_boto3_session_db_cluster(
        self, session: Boto3Session
    ) -> Dict[str, Any]:
        """
        This function is primarily used to test connectivity for a boto3
        session
        """
        rds: Any = session.client("rds", region_name=POSTRGRESQL_AWS_REGION)
        try:
            return rds.describe_db_clusters(
                DBClusterIdentifier=self.postgresql_db_cluster_identifier
            )["DBClusters"][0]
        except rds.exceptions.DBClusterNotFoundFault as error:
            permission_error: PermissionError = PermissionError(
                get_exception_text()
            )
            setattr(permission_error, "original_error", error)
            raise permission_error

    def _get_postgresql_assumed_role_boto3_session(
        self, profile_name: Optional[str] = None
    ) -> Boto3Session:
        """
        Get a boto3 session using the appropriate assumed role ARN
        """
        #  arn: str = self.postgresql_arn
        credentials: Dict[str, Any]
        arn: str = _get_aws_role_arn()
        role_session_name: str
        session: Boto3Session = Boto3Session(profile_name=profile_name)
        if arn:
            web_identity_token: str = _get_web_identity_token()
            role_session_name = _get_assume_role_session_name()
            log.info(
                f'Assuming role "{arn}" with session name '
                f'"{role_session_name}"'
            )
            if web_identity_token:
                credentials = session.client(
                    "sts"
                ).assume_role_with_web_identity(
                    RoleArn=arn,
                    RoleSessionName=role_session_name,
                    WebIdentityToken=web_identity_token,
                    DurationSeconds=ASSUME_ROLE_DURATION_SECONDS,
                )[
                    "Credentials"
                ]
            else:
                credentials = session.client("sts").assume_role(
                    RoleArn=arn,
                    RoleSessionName=role_session_name,
                    DurationSeconds=ASSUME_ROLE_DURATION_SECONDS,
                )["Credentials"]
            session = Boto3Session(
                aws_access_key_id=credentials["AccessKeyId"],
                aws_secret_access_key=credentials["SecretAccessKey"],
                aws_session_token=credentials["SessionToken"],
            )
        role_session_name = _get_assume_role_session_name()
        log.info(
            f'Assuming role "{self.postgresql_arn}" with session name '
            f'"{role_session_name}"'
        )
        credentials = session.client("sts").assume_role(
            RoleArn=self.postgresql_arn,
            RoleSessionName=role_session_name,
            DurationSeconds=ASSUME_ROLE_DURATION_SECONDS,
        )["Credentials"]
        session = Boto3Session(
            region_name=POSTRGRESQL_AWS_REGION,
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
        )
        assert self._describe_boto3_session_db_cluster(session=session)
        return session

    @property  # type: ignore
    @work_boto3_session_lru_cache()
    def postgresql_boto3_session(self) -> Boto3Session:
        """
        Return a boto3 session for connecting to the waffle-iron AWS account
        from which our PostgreSQL database is served
        """
        assert self.environment in POSTGRESQL_ENVIRONMENTS
        profile_name: Optional[str]
        error_messages: List[str] = []
        for profile_name in chain(Boto3Session().available_profiles, (None,)):
            log.info(
                f'Attempting to use profile_name "{profile_name}"'
                if profile_name
                else "Attempting to use the default profile_name"
            )
            try:
                return (
                    Boto3Session(
                        profile_name=profile_name,
                        region_name=POSTRGRESQL_AWS_REGION,
                    )
                    if profile_name
                    else self._get_postgresql_assumed_role_boto3_session()
                )
            except (
                BotoCoreNoCredentialsError,
                BotoCoreClientError,
                BotoCoreHTTPClientError,
                PermissionError,
            ):
                error_messages.append(
                    f"{profile_name}: {get_exception_text()}"
                )
        raise PermissionError("\n".join(error_messages))

    def _set_table_tsv_content_encoding(self, table_name: str) -> None:
        directory: str = f"{API_CSV_DIRECTORY}{table_name}/"

        def set_tsv_content_encoding(path: str) -> None:
            if self.echo:
                log.info(f"Setting TSV content encoding for {path}")
            if TYPE_CHECKING:
                assert isinstance(self.file_system, SimpleStorageService)
            self.file_system.update_metadata(
                path,
                {
                    "Content-Encoding": "gzip",
                    "Content-Type": "text/tab-separated-values",
                },
            )

        # Set the Content-Encoding for all CSVs
        deque(
            map(
                set_tsv_content_encoding,
                filter(_is_csv, self.file_system.iter_file_paths(directory)),
            ),
            maxlen=0,
        )

    def extract_table(self, table_name: str) -> None:
        """
        Extract data from Snowflake corresponding to the specified
        PostgreSQL table.

        Parameters:

        - table_name (str)
        """
        # Touch the PostgreSQL session to bind it to the base
        getattr(self, "postgresql_session")
        cls: Type[APIBase] = get_base_table_name_subclass(APIBase, table_name)
        select_statement: str = (
            get_bind_snowflake_view_select_statement(
                self.snowflake_session.bind,
                table_name,
                directory=_SNOWFLAKE_QUERIES_DIRECTORY,
            )
            or ""
        )
        assert select_statement
        directory: str = f"{API_CSV_DIRECTORY}{table_name}/"
        # Remove the "/_SUCCESS" file, so that other jobs know this
        # table's data is incomplete/loading
        self.file_system.delete_success(directory)
        # Identify the query IDs represented in the target directory

        def get_query_ids() -> Set[str]:
            return set(
                filter(
                    None,
                    map(
                        _get_extract_file_name_query_id,
                        self.file_system.iter_file_paths(directory),
                    ),
                )
            )

        location: str = f"@{STAGE_NAME}{API_CSV_DIRECTORY}{table_name}/"
        old_query_ids: Set[str] = get_query_ids()
        # Copy the data from Snowflake into S3
        self.snowflake_copy_into_location(
            select_statement=select_statement,
            location=location,
            column_names=get_class_column_names(cls),
            format="TSV",
        )
        new_query_ids: Set[str] = get_query_ids() - old_query_ids
        # If there are no new query IDs, nothing was extracted
        if not new_query_ids:
            raise FileNotFoundError(
                "No new data was found in "
                f"{self.file_system.get_absolute_path(directory)}"
            )
        if len(new_query_ids) > 1:
            raise RuntimeError(
                "Too much new data was found. New query IDs: {}".format(
                    tuple(new_query_ids)
                )
            )
        log.info(
            f"{table_name} extract finished! Query ID: "
            f"{tuple(new_query_ids)[0]}"
        )
        log.info(
            "Cleaning up files from old {} queries: {}".format(
                table_name, tuple(old_query_ids)
            )
        )
        # Delete old files
        query_id: str
        for query_id in old_query_ids:
            # the FileSystem.delete_directory method also works for *prefixes*
            # with the S3 file system
            prefix = f"{directory}data_{query_id}_"
            self.file_system.delete_directory(prefix)
        self._set_table_tsv_content_encoding(table_name)
        # Add a "/_SUCCESS" file, so that other jobs know this
        # table's data is complete/whole
        self.file_system.put_success(directory)

    @retry(
        (DBAPIError,),
        number_of_attempts=3,
    )
    def postgresql_execute(self, statement: str) -> None:
        self.postgresql_session.begin()
        try:
            self.postgresql_session.execute(statement)
            self.postgresql_session.commit()
        except Exception:
            log.error(get_exception_text())
            self.postgresql_session.rollback()
            raise

    def _iter_postgresql_table_indexes_ddl(
        self, table: str, schema: str = "public"
    ) -> Iterable[str]:
        """
        Parameters:

        - table (str)
        - schema (str)

        Returns: An iterator yielding DDL to re-create indexes for the
        specified `table`.
        """
        row: Row
        for row in self.postgresql_session.execute(
            "select pg_get_indexdef(idx.oid)||';'"
            "from pg_index ind "
            "join pg_class idx on idx.oid = ind.indexrelid "
            "join pg_class tbl on tbl.oid = ind.indrelid "
            "left join pg_namespace ns on ns.oid = tbl.relnamespace "
            f"where tbl.relname = '{table}' "
            f"and ns.nspname = '{schema}' "
        ):
            # Modify the DDL so that the index name is not explicitly
            # specified
            yield re.sub(
                r"^(CREATE(?: UNIQUE)? INDEX)(?: [^ ]+)?( ON)\b",
                r"\1\2",
                row[0],
                flags=re.IGNORECASE,
            )


def _iter_table_names() -> Iterable[str]:
    file_name: str
    return map(
        lambda file_name: file_name.partition(".")[0],
        filter(
            lambda file_name: (file_name.rpartition(".")[-1].lower() == "sql"),
            os.listdir(_SNOWFLAKE_QUERIES_DIRECTORY),
        ),
    )


class Broker(_Broker):
    """
    This class brokers exchange of data between systems and distributes
    tasks to instances of `Work`.

    Parameters:

    - environment (str): "dev", "qa", or "prod"
    - parallelism (int) = 0: If this is 0, the default parallelism for
      the Spark cluster will be used.
    - concurrency (analytics_etl.concurrency.Concurrency)
      = analytics_etl.concurrency.Concurrency.SPARK
    - echo (bool) = False: If `True`, all logging will be printed to the
      console.
    """

    work: Work

    def __init__(
        self,
        environment: str = "",
        parallelism: Optional[int] = None,
        concurrency: Concurrency = Concurrency.MULTIPROCESSING,
        echo: bool = False,
    ) -> None:
        super().__init__(
            environment=environment,
            parallelism=parallelism,
            concurrency=concurrency,
            echo=echo,
            work=Work(
                environment=environment,
                echo=echo,
            ),
        )

    def extract(
        self,
        concurrency: Optional[Concurrency] = None,
        parallelism: Optional[int] = None,
    ) -> None:
        """
        Extract data from Snowflake to S3.

        Parameters:

        - concurrency (analytics_etl.concurrency.Concurrency) = None:
          If not provided, this will default to the class'es concurrency
          type
        - parallelism (int) = None
        """
        self.map(
            self.work.extract_table,
            _iter_table_names(),
            parallelism=parallelism,
            concurrency=concurrency,
        )

    def load(self) -> None:
        """
        Load data from S3 to PostgreSQL for all applicable tables.
        """
        self.map(
            self.load_table,
            _iter_table_names(),
            # We don't want to load multiple *tables* in parallel,
            # as all resources will be utilized to parallelize
            # loading of individual files into each table
            concurrency=Concurrency.NONE,
        )

    def load_table(self, table_name: str) -> None:
        """
        This function...
        1. Loads all of the data for a PostgreSQL table into a temporary table
           (one which mimics the target, but without indexes/constraints/etc.)
        2. Populates a newly created (empty) swap table, one which *does*
           have indices/constraints/etc., from the contents of the
           temporary table
        3. Swaps out the target table with the swap table, using
           `ALTER TABLE ... RENAME TO`
        4. Drops the temporary and old tables, leaving the swap table as
           replacement

        Parameters:

        - table_name (str)
        """
        # Important: `self.work.postgresql_session` must be accessed before
        # accessing `Base`
        postgresql_session: Session = self.work.postgresql_session
        log.info(f"Loading {table_name} into PostgreSQL")
        cls: Type[APIBase] = get_base_table_name_subclass(APIBase, table_name)
        swap_table_name: str = f"_SWAP_{table_name}"
        old_table_name: str = f"_OLD_{table_name}"
        table_path: str = f"{API_CSV_DIRECTORY}{table_name}/"
        # Ensure there is not another load in-progress
        if not self.work.file_system.had_success(table_path):
            raise FileNotFoundError(self.work.file_system.get_url(table_path))
        # Import data from S3
        # Table names need to be quoted since they are uppercase
        dialect: Dialect = postgresql_session.bind.engine.dialect
        preparer: IdentifierPreparer = getattr(dialect, "preparer")(dialect)
        quoted_table_name: str = preparer.quote(table_name)
        quoted_swap_table_name: str = preparer.quote(swap_table_name)
        quoted_old_table_name: str = preparer.quote(old_table_name)
        quoted_column_names: str = ",".join(
            map(preparer.quote, get_class_column_names(cls))
        )
        log.info("Creating swap table...")
        postgresql_session.begin()
        # Create the swap table
        deque(
            map(
                postgresql_session.execute,
                (
                    # Check for, and drop if found, swap tables which might
                    # remain from a failed job
                    f"DROP TABLE IF EXISTS {quoted_swap_table_name} CASCADE",
                    # Create the swap table
                    f"CREATE TABLE {quoted_swap_table_name} ("
                    f"LIKE {quoted_table_name} "
                    # Include everything from the original table except indexes
                    "INCLUDING DEFAULTS "
                    "INCLUDING CONSTRAINTS "
                    "INCLUDING STORAGE "
                    "INCLUDING COMMENTS"
                    ")",
                ),
            ),
            maxlen=0,
        )
        postgresql_session.commit()
        log.info("...swap table created successfully")
        # Construct the import statements

        def get_select_statement(path: str) -> str:
            if TYPE_CHECKING:
                assert isinstance(self.work.file_system, SimpleStorageService)
            absolute_path: str = self.work.file_system.get_absolute_path(path)
            return (
                "SELECT aws_s3.table_import_from_s3("
                f"'{quoted_swap_table_name}', "
                f"'{quoted_column_names}', "
                "'(format text)', "
                "aws_commons.create_s3_uri("
                f"'{self.work.file_system.bucket_name}', "
                f"'{absolute_path}', "
                f"'{POSTRGRESQL_AWS_REGION}'"
                ")"
                ")"
            )

        log.info("Assembling S3 import statements...")
        import_statements: Tuple[str, ...] = tuple(
            map(
                get_select_statement,
                filter(
                    _is_csv, self.work.file_system.iter_file_paths(table_path)
                ),
            )
        )
        log.info("...S3 import statements assembled")
        # Execute the import statements in parallel
        deque(
            self.map(
                self.work.postgresql_execute,
                import_statements,
                parallelism=min(len(import_statements), MAX_PROCESSES),
            ),
            maxlen=0,
        )
        log.info("...finished executing S3 import statements")

        def substitute_swap_table_name(statement: str) -> str:
            return statement.replace(quoted_table_name, quoted_swap_table_name)

        # Get rid of all open connections
        log.info("Disposing of all open connections...")
        postgresql_session.bind.engine.dispose()
        log.info("...open connections have been disposed of")
        # Get the DDL required to re-create indexes
        log.info("Assembling statements to re-create indexes...")
        recreate_indexes_statements: Tuple[str, ...] = tuple(
            map(
                substitute_swap_table_name,
                self.work._iter_postgresql_table_indexes_ddl(table=table_name),
            )
        )
        log.info("...statements to re-create indexes have been assembled")
        # Create a fresh session
        type(self.work).postgresql_session.fget.cache_clear()  # type: ignore
        postgresql_session = self.work.postgresql_session
        # Swap the tables
        log.info("Beginning the swap...")
        postgresql_session.begin()
        try:
            deque(
                map(
                    postgresql_session.execute,
                    recreate_indexes_statements
                    + (
                        # Cleanup leftovers from previous attempts
                        (
                            f"DROP TABLE IF EXISTS {quoted_old_table_name} "
                            "CASCADE"
                        ),
                        (
                            # Swap out the old table for the new one
                            f"ALTER TABLE {quoted_table_name} "
                            f"RENAME TO {quoted_old_table_name};\n"
                            f"ALTER TABLE {quoted_swap_table_name} "
                            f"RENAME TO {quoted_table_name}"
                        ),
                    ),
                ),
                maxlen=0,
            )
            log.info("...committing the swap...")
            postgresql_session.commit()
        except Exception:
            log.error(f"...swap failed:\n{get_exception_text()}")
            postgresql_session.rollback()
            raise
        log.info("Attempting to re-create views...")
        # Re-create views, since those based on this table will have been
        # dropped
        postgresql_session.begin()
        connection: Connection
        if isinstance(postgresql_session.bind, Engine):
            connection = postgresql_session.bind.connect()
        else:
            assert isinstance(postgresql_session.bind, Connection)
            connection = postgresql_session.bind
        create_postgresql_environment(
            self.work.environment.rpartition("-")[-1],
            bind=connection,
            views_only=True,
            checkfirst=True,
            echo=self.work.echo,
        )
        postgresql_session.commit()
        postgresql_session.begin()
        log.info("Verifying views were re-created successfully...")
        # Verify that all views have been re-created
        view: Type[APIBase]
        for view in filter(
            lambda view: view.__table__.info.get("is_view", False),
            iter_base_sorted_subclasses(APIBase),
        ):
            view_name: str = get_class_table_name(view)  # type: ignore
            log.info(f"Verifying that {view_name} exists.")
            row: Optional[Row] = connection.execute(
                select(view).limit(1)
            ).fetchone()
            if not row:
                raise RuntimeError(
                    f"Missing view: {view_name}"  # type: ignore
                )
            log.info(f"Confirmed! {view_name} exists.")
        log.info("Confirmed! Views were re-created successfully")
        postgresql_session.commit()
        # Close open connections
        log.info("Disposing of all open connections...")
        connection.engine.dispose()
        log.info("...open connections have been disposed of")
        # Create a fresh session
        type(self.work).postgresql_session.fget.cache_clear()  # type: ignore
        postgresql_session = self.work.postgresql_session
        postgresql_session.begin()
        # Drop the old table (with no CASCADE, to ensure the old table is no
        # longer referenced by any views, now that we've re-created them)
        postgresql_session.execute(text(f"DROP TABLE {quoted_old_table_name}"))
        postgresql_session.commit()

    def main(
        self,
        concurrency: Optional[Concurrency] = None,
        parallelism: Optional[int] = None,
    ) -> None:
        self.extract(concurrency=concurrency, parallelism=parallelism)
        self.load()
