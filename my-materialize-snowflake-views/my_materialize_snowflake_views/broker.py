import os
from itertools import chain
from typing import Any, Iterable, Optional, Set, Tuple, Type

from analytics_etl.concurrency import Concurrency
from analytics_orm.declarative import (
    get_base_table_name_subclass,
    get_class_column_names,
    get_class_primary_key_and_column_names,
    get_class_qualified_table_name,
)
from analytics_orm.utilities import is_ci
from my_datastore_etl.broker import Broker as _Broker
from my_datastore_etl.broker import Work as _Work
from my_datastore_etl.broker import log
from my_datastore_etl.utilities import retry
from my_datastore_model.base import Base
from my_datastore_model.view import (
    get_bind_snowflake_view_select_statement,
)
from sqlalchemy import func, select  # type: ignore
from sqlalchemy.engine.base import Connection  # type: ignore
from sqlalchemy.engine.result import Result  # type: ignore
from sqlalchemy.engine.row import Row  # type: ignore
from sqlalchemy.exc import DBAPIError  # type: ignore
from sqlalchemy.exc import ProgrammingError  # type: ignore

from .config import DEFAULT_CONCURRENCY, TABLES_CHANGE_TRACKING_COLUMNS

_SELECT_STATEMENTS_DIRECTORY: str = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "_select_statements"
)


def _iter_table_names(
    include: Tuple[str, ...], exclude: Tuple[str, ...]
) -> Iterable[str]:
    def include_table(table_name: str) -> bool:
        return ((not include) or (table_name in include)) and (
            (not exclude) or (table_name not in exclude)
        )

    file_name: str
    return filter(
        include_table,
        map(
            lambda file_name: file_name.partition(".")[0],
            filter(
                lambda file_name: file_name.rpartition(".")[-1].lower()
                == "sql",
                os.listdir(_SELECT_STATEMENTS_DIRECTORY),
            ),
        ),
    )


def _get_wrapped_count_statement(statement: str) -> str:
    count_statement: str = (
        f"SELECT COUNT(*) as num_rows FROM ({statement}) subquery"
    )
    return count_statement


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


def get_connection_select_statement(
    connection: Connection, table_name: str
) -> str:
    connection.exec_driver_sql("USE SECONDARY ROLES ALL")
    connection.exec_driver_sql("COMMIT")
    cls: Type[Base] = get_base_table_name_subclass(Base, table_name)
    qualified_table_name: str = get_class_qualified_table_name(cls)
    select_statement: str = (
        get_bind_snowflake_view_select_statement(
            connection,
            table_name,
            directory=_SELECT_STATEMENTS_DIRECTORY,
        )
        or ""
    )
    primary_key_column_names: Tuple[str, ...]
    other_column_names: Tuple[str, ...]
    (
        primary_key_column_names,
        other_column_names,
    ) = get_class_primary_key_and_column_names(cls)
    # Add change tracking timestamps
    cte_name: str = f"{table_name}_CTE"
    column_name: str
    if table_name in TABLES_CHANGE_TRACKING_COLUMNS:
        change_tracking_column_name: str = TABLES_CHANGE_TRACKING_COLUMNS[
            table_name
        ]
        other_column_names = tuple(
            filter(
                lambda column_name: (
                    column_name != change_tracking_column_name
                ),
                other_column_names,
            )
        )
        join_conditions: Iterable[str] = map(
            lambda column_name: (
                f'{cte_name}."{column_name}" = '
                f'{qualified_table_name}."{column_name}"'
            ),
            primary_key_column_names,
        )
        changed_or_conditions: Iterable[str] = chain(
            (
                (
                    f"{qualified_table_name}."
                    f'"{change_tracking_column_name}" IS NULL'
                ),
            ),
            map(
                lambda column_name: (
                    f'{cte_name}."{column_name}" IS DISTINCT FROM '
                    f'{qualified_table_name}."{column_name}"'
                ),
                other_column_names,
            ),
        )
        column_expressions: Iterable[str] = chain(
            map(
                lambda column_name: f'{cte_name}."{column_name}"',
                primary_key_column_names + other_column_names,
            ),
            (
                (
                    f"CASE WHEN "
                    f"{' OR '.join(changed_or_conditions)} THEN "
                    "SYSDATE() ELSE "
                    f"{qualified_table_name}."
                    f'"{change_tracking_column_name}" END '
                    f"AS {change_tracking_column_name}"
                ),
            ),
        )
        select_statement = (
            f"WITH {cte_name} AS (\n"
            f"{select_statement}\n"
            ")\n"
            f"SELECT {', '.join(column_expressions)} "
            f"FROM {cte_name}\n"
            f"LEFT OUTER JOIN {qualified_table_name}\n"
            f"ON {' AND '.join(join_conditions)}\n"
        )
    return select_statement


class Work(_Work):
    """
    This class encapsulates work to be performed by individual processes in a
    multi-process pool.

    Parameters:

    - environment (str)
    - echo (bool)
    """

    @retry((DBAPIError,), number_of_attempts=5)
    def materialize_table(
        self, table_name: str, _column_names: Tuple[str, ...] = ()
    ) -> None:
        """
        Truncate a table and populate it from a query of the same name
        """
        # The Snowflake session must be accessed at the start in order
        # to bind it to `Base`
        connection: Connection = self.snowflake_session.bind.connect()
        select_statement: str = get_connection_select_statement(
            connection, table_name
        )
        # Assemble and log our `INSERT INTO` statement
        cls: Type[Base] = get_base_table_name_subclass(Base, table_name)
        qualified_table_name: str = get_class_qualified_table_name(cls)
        column_names: Tuple[str, ...] = _column_names
        if not column_names:
            column_names = get_class_column_names(cls)
        quoted_column_names: str = ", ".join(
            f'"{column_name}"' for column_name in column_names
        )
        command: str = (
            f"INSERT OVERWRITE INTO {qualified_table_name} "
            f"({quoted_column_names})\n"
            f"SELECT {quoted_column_names} FROM ({select_statement})"
        )
        # Execute the statement and log the response
        row: Row
        rows: Iterable[Row]
        try:
            rows = connection.exec_driver_sql(command)
        except ProgrammingError:
            if _column_names:
                raise
            # Identify the column names returned by the SELECT statement
            result: Result = connection.exec_driver_sql(select_statement)
            row = result.first()
            select_column_names: Set[str] = set(row._fields)
            # Filter out column names identified by the model
            # which are not in the select statement
            column_names = tuple(
                filter(select_column_names.__contains__, column_names)
            )
            if not column_names:
                raise
            return self.materialize_table(table_name, column_names)
        for row in rows:
            repr_row: str = repr(row)
            if repr_row.strip("{}() "):
                log.info(repr_row)
        self.snowflake_session.commit()
        if not is_ci():
            self.extract_table(table_name)

    @retry((DBAPIError,), number_of_attempts=5)
    def extract_table(self, table_name: str) -> None:
        """
        Extract data from Snowflake to S3
        Parameters:
        - table_name (str)
        """
        assert self.file_system
        cls: Type[Base] = get_base_table_name_subclass(Base, table_name)
        select_statement: str = (
            get_bind_snowflake_view_select_statement(
                self.snowflake_session.bind,
                table_name,
                directory=_SELECT_STATEMENTS_DIRECTORY,
            )
            or ""
        )
        assert select_statement
        directory: str = f"{self.tables_directory}{table_name}/"
        # Remove the "/_SUCCESS" file, so that other jobs know this
        # table's data is incomplete/loading
        self.file_system.delete_success(directory)

        def get_query_ids() -> Set[str]:
            """
            Identify the query IDs represented in the target directory
            """
            assert self.file_system
            return set(
                filter(
                    None,
                    map(
                        _get_extract_file_name_query_id,
                        self.file_system.iter_file_paths(directory),
                    ),
                )
            )

        old_query_ids: Set[str] = get_query_ids()
        # Copy the data from Snowflake into S3
        self.snowflake_copy_into_location(
            select_statement=select(cls),
            location=(
                f"@{self.snowflake_s3_stage_name}/"
                f"{self.tables_directory}{table_name}/"
            ),
            column_names=get_class_column_names(cls),
            format="PARQUET",
        )
        new_query_ids: Set[str] = get_query_ids() - old_query_ids
        # If there are no new query IDs, nothing was extracted
        if not new_query_ids:
            log.info(
                "No new data was found in "
                f"{self.file_system.get_absolute_path(directory)}"
            )
            self.file_system.put_success(directory)
            return
        if len(new_query_ids) > 1:
            raise RuntimeError(
                f"Too much new data was found for {table_name} "
                f"New query IDs: {','.join(new_query_ids)}"
            )
        stage_select_statement: str = _get_wrapped_count_statement(
            self.get_table_stage_select_statement(table_name)
        )
        log.info(f"Extract finished! Query ID: {tuple(new_query_ids)[0]}")
        log.info(
            "Cleaning up files from old queries:\n{}".format(
                "\n".join(old_query_ids)
            )
        )
        # Delete old files
        query_id: str
        for query_id in old_query_ids:
            # the FileSystem.delete_directory method also works for *prefixes*
            # with the S3 file system
            prefix = f"{directory}data_{query_id}_"
            self.file_system.delete_directory(prefix)
        # Lookup the number of rows in S3
        first_row: Optional[Row] = self.snowflake_session.execute(
            stage_select_statement
        ).first()
        assert first_row
        stage_row_count: int = first_row[0]
        # Lookup the number of rows in Snowflake
        first_row = self.snowflake_session.execute(
            select(func.count(cls.__table__.columns[0]))
        ).first()
        assert first_row
        table_row_count: int = first_row[0]
        assert (
            stage_row_count == table_row_count
        ), f"Mismatch in rows found between stage and table for {table_name}"
        # Add a "/_SUCCESS" file, so that other jobs know this
        # table's data is complete/whole
        self.file_system.put_success(directory)


class Broker(_Broker):
    work: Work

    def __init__(
        self,
        environment: str,
        concurrency: Concurrency = DEFAULT_CONCURRENCY,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            environment=environment,
            concurrency=concurrency,
            work=Work,
            **kwargs,
        )

    def materialize(
        self,
        concurrency: Optional[Concurrency] = None,
        parallelism: Optional[int] = None,
        include: Tuple[str, ...] = (),
        exclude: Tuple[str, ...] = (),
    ) -> None:
        """
        Refresh "materialized" views.

        Parameters:

        - concurrency (analytics_etl.concurrency.Concurrency) = None:
          If not provided, this will default to the class'es concurrency
          type
        - parallelism (int) = None
        """
        self.map(
            self.work.materialize_table,
            _iter_table_names(include, exclude),
            parallelism=parallelism,
            concurrency=concurrency,
        )
