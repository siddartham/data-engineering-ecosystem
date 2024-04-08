import re
from typing import Any, Dict, List, Match, Optional, Pattern, Sequence, Union

from pyhive.hive import Cursor as HiveCursor  # type: ignore
from sqlalchemy import event  # type: ignore
from sqlalchemy.engine import Connection, Engine  # type: ignore
from sqlalchemy.engine.interfaces import ExecutionContext  # type: ignore

from .utilities import get_bind_dialect_name

__all__: List[str] = ["listen_and_drop_table_before_create"]


_CREATE_EXTERNAL_TABLE_PATTERN: Pattern = re.compile(
    r"^(\s*)CREATE\s+EXTERNAL\s+TABLE\s+`([^`]+)`", flags=re.IGNORECASE
)


def listen_and_drop_table_before_create(
    bind: Union[Engine, Connection]
) -> None:
    """
    This function establishes a listener for connection events, and if the
    `bind` is for a *hive* connection, looks for "CREATE EXTERNAL TABLE"
    statements, and drops those tables prior to executing the "create"
    statement.

    Parameters:

    - **bind** (sqlalchemy.engine.interfaces.Connectable)
    """

    def drop_table_before_create_table_cursor_execute(
        connection: Connection,
        cursor: HiveCursor,
        statement: str,
        parameters: Union[Dict[str, Any], Sequence[Any]],
        context: ExecutionContext,
        executemany: bool,
    ) -> None:
        """
        This function should be executed by a connection listener on the
        "before_cursor_execute" event, in order to drop tables (if they exist)
        prior to creation.
        """
        dialect_name: str = get_bind_dialect_name(connection)
        if dialect_name == "hive":
            create_external_table_match: Optional[
                Match
            ] = _CREATE_EXTERNAL_TABLE_PATTERN.search(statement)
            if create_external_table_match:
                table_name: str = create_external_table_match.groups()[-1]
                connection.execute(f"DROP TABLE IF EXISTS `{table_name}`")

    dialect_name: str = get_bind_dialect_name(bind)
    if dialect_name == "hive":
        event.listen(
            bind,
            "before_cursor_execute",
            drop_table_before_create_table_cursor_execute,
        )
