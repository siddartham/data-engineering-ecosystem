from logging import Logger
from typing import Iterable, List, Optional

from alembic.autogenerate import comparators, renderers  # type: ignore
from alembic.autogenerate.api import AutogenContext  # type: ignore
from alembic.operations.ops import (  # type: ignore
    AddColumnOp,
    AlterColumnOp,
    MigrateOperation,
    ModifyTableOps,
)
from sqlalchemy import Table  # type: ignore

from ..utilities import add_log_stream_handler, get_dialect_name
from .operations import AddPrimaryKeyOp, DropPrimaryKeyOp

__all__: List[str] = ["comparators", "compare_primary_key"]

log: Logger = add_log_stream_handler()


@comparators.dispatch_for("table")
def databricks_modify_column_nullability(
    autogen_context: AutogenContext,
    modify_table_ops: ModifyTableOps,
    schema: str,
    tname: str,
    conn_table: Optional[Table],
    metadata_table: Optional[Table],
) -> None:
    """
    New columns added to a Databricks table must be nullable. This function
    modifies the column nullability to be nullable if it is not already.
    """
    dialect_name: str = get_dialect_name(autogen_context.dialect)

    if dialect_name == "databricks":
        operation: MigrateOperation
        for operation in modify_table_ops.ops:
            if isinstance(operation, AddColumnOp):
                if operation.column.nullable is False:
                    operation.column.nullable = True

                    modify_table_ops.ops.append(
                        AlterColumnOp(
                            table_name=operation.table_name,
                            column_name=operation.column.name,
                            modify_nullable=False,
                            schema=operation.schema,
                        )
                    )


@comparators.dispatch_for("table")
def compare_primary_key(
    autogen_context: AutogenContext,
    modify_table_ops: ModifyTableOps,
    schema: str,
    tname: str,
    conn_table: Optional[Table],
    metadata_table: Optional[Table],
) -> None:
    """
    When there is a primary key change, this function drops the existing
    primary key and replaces it with a new one
    """
    if (
        (metadata_table is not None)
        and (conn_table is not None)
        and set(column.name for column in conn_table.primary_key)
        != set(column.name for column in metadata_table.primary_key)
    ):
        log.info(
            f"Primary key changed for {conn_table.name}:\n"
            f"{repr(conn_table.primary_key)}\n"
            " -> \n"
            f"{repr(metadata_table.primary_key)}"
        )
        if conn_table.primary_key:
            modify_table_ops.ops.append(
                DropPrimaryKeyOp.from_constraint(conn_table.primary_key)
            )
        modify_table_ops.ops.append(
            AddPrimaryKeyOp.from_constraint(metadata_table.primary_key)
        )


def _iter_add_primary_key(operation: AddPrimaryKeyOp) -> Iterable[str]:
    yield (
        "op.add_primary_key(  # type: ignore\n"
        f'  table_name="{operation.table_name}",\n'
        f"  column_names={operation.column_names},"
    )
    if operation.schema:
        yield f'  schema="{operation.schema}",'
    yield ")"


@renderers.dispatch_for(AddPrimaryKeyOp)
def _add_primary_key(
    autogen_context: AutogenContext, operation: AddPrimaryKeyOp
) -> str:
    return "\n".join(_iter_add_primary_key(operation))


def _iter_drop_primary_key(operation: DropPrimaryKeyOp) -> Iterable[str]:
    yield (
        "op.drop_primary_key(  # type: ignore\n"
        f'  table_name="{operation.table_name}",\n'
        f"  column_names={operation.column_names},"
    )
    if operation.schema:
        yield f'  schema="{operation.schema}",'
    yield ")"


@renderers.dispatch_for(DropPrimaryKeyOp)
def _drop_primary_key(
    autogen_context: AutogenContext, operation: DropPrimaryKeyOp
) -> str:
    return "\n".join(_iter_drop_primary_key(operation))
