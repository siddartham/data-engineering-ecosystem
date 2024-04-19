from logging import Logger
from types import ModuleType
from typing import Dict, Iterable, Optional

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
from .operations import (
    AddPrimaryKeyOp,
    DropPrimaryKeyOp,
    SetTagsOp,
    UnsetTagsOp,
)

_databricks: Optional[ModuleType]
__databricks: Optional[ModuleType]
try:
    from .. import databricks as __databricks  # noqa
    from . import databricks as _databricks  # noqa
except ImportError:
    databricks = None

_snowflake: Optional[ModuleType]
__snowflake: Optional[ModuleType]
try:
    from .. import snowflake as __snowflake  # noqa
    from . import snowflake as _snowflake  # noqa
except ImportError:
    snowflake = None

log: Logger = add_log_stream_handler()


@comparators.dispatch_for("table")
def _compare_table(  # noqa: C901
    autogen_context: AutogenContext,
    modify_table_ops: ModifyTableOps,
    schema: str,
    tname: str,
    conn_table: Optional[Table],
    metadata_table: Optional[Table],
) -> None:
    """
    This function adds custom comparison logic for tables
    """
    # When there is a primary key change, the following drops the existing
    # primary key and replaces it with a new one
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

    dialect_name: str = get_dialect_name(autogen_context.dialect)
    # New columns added to a Databricks table must be nullable. The following
    # modifies the column nullability to be nullable if it is not already.
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

        if metadata_table is not None and conn_table is not None:
            metadata_table_tags: Dict[str, str] = metadata_table.info.get(
                "tags", {}
            )
            conn_table_tags: Dict[str, str] = conn_table.info.get("tags", {})

            if metadata_table_tags != conn_table_tags:
                tags_to_remove: Dict[str, str] = {
                    tag_name: tag_value
                    for tag_name, tag_value in conn_table_tags.items()
                    if tag_name not in metadata_table_tags
                }
                tags_to_add: Dict[str, str] = {
                    tag_name: tag_value
                    for tag_name, tag_value in metadata_table_tags.items()
                    if tag_name not in conn_table_tags
                    or tag_value != conn_table_tags[tag_name]
                }
                if tags_to_remove:
                    modify_table_ops.ops.append(
                        UnsetTagsOp(
                            table_name=conn_table.name,
                            tags=tags_to_remove,
                        )
                    )
                if tags_to_add:
                    modify_table_ops.ops.append(
                        SetTagsOp(
                            table_name=conn_table.name,
                            tags=tags_to_add,
                        )
                    )
                log.info(
                    f"Detected tag differences for {metadata_table.name}:\n"
                    f"Tags to remove: {tags_to_remove}\n"
                    f"Tags to add: {tags_to_add}"
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


def _iter_set_tags(operation: SetTagsOp) -> Iterable[str]:
    yield (
        "op.set_tags(  # type: ignore\n"
        f'  table_name="{operation.table_name}",\n'
        f"  tags={operation.tags},"
    )
    if operation.schema:
        yield f'  schema="{operation.schema}",'
    yield ")"


def _iter_unset_tags(operation: UnsetTagsOp) -> Iterable[str]:
    yield (
        "op.unset_tags(  # type: ignore\n"
        f'  table_name="{operation.table_name}",\n'
        f"  tags={operation.tags},"
    )
    if operation.schema:
        yield f'  schema="{operation.schema}",'
    yield ")"


@renderers.dispatch_for(SetTagsOp)
def _set_tags(autogen_context: AutogenContext, operation: SetTagsOp) -> str:
    return "\n".join(_iter_set_tags(operation))


@renderers.dispatch_for(UnsetTagsOp)
def _unset_tags(
    autogen_context: AutogenContext, operation: UnsetTagsOp
) -> str:
    return "\n".join(_iter_unset_tags(operation))
