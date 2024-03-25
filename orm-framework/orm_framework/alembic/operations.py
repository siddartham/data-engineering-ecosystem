from typing import Iterator, Optional, Sequence, Tuple, Union

from alembic.operations import Operations, schemaobj  # type: ignore
from alembic.operations.ops import AlterTableOp  # type: ignore
from alembic.runtime.migration import MigrationContext  # type: ignore
from sqlalchemy import Column, PrimaryKeyConstraint, Table  # type: ignore

from ..ddl import AddPrimaryKey, DropPrimaryKey
from ..utilities import get_class_qualified_name


@Operations.register_operation("add_primary_key")
class AddPrimaryKeyOp(AlterTableOp):
    __slots__: Tuple[str, ...] = ("table_name", "schema", "column_names")

    def __init__(
        self,
        table_name: str,
        schema: Optional[str] = None,
        column_names: Union[Iterator[str], Sequence[str]] = (),
    ) -> None:
        super().__init__(table_name, schema=schema)
        self.column_names: Tuple[str, ...] = tuple(column_names)

    @classmethod
    def add_primary_key(
        cls,
        operations: Operations,
        table_name: str,
        schema: Optional[str] = None,
        column_names: Union[Iterator[str], Sequence[str]] = (),
    ) -> None:
        operations.invoke(cls(table_name, schema, column_names))

    def reverse(self) -> "DropPrimaryKeyOp":
        return DropPrimaryKeyOp(
            table_name=self.table_name,
            schema=self.schema,
            column_names=self.column_names,
        )

    def to_table(
        self, migration_context: Optional[MigrationContext] = None
    ) -> Table:
        schema_obj: schemaobj.SchemaObjects = schemaobj.SchemaObjects(
            migration_context
        )
        return schema_obj.table(self.table_name, schema=self.schema)

    def to_diff_tuple(self) -> Tuple[str, Table]:
        return "add_primary_key", self.to_table()

    @classmethod
    def from_constraint(
        cls, primary_key_constraint: PrimaryKeyConstraint
    ) -> "AddPrimaryKeyOp":
        column: Column
        return cls(
            primary_key_constraint.table.name,
            schema=primary_key_constraint.table.schema,
            column_names=(
                column.name for column in primary_key_constraint.columns
            ),
        )

    def __repr__(self) -> str:
        return (
            f"{get_class_qualified_name(type(self))}(\n"
            f"    table_name={repr(self.table_name)},\n"
            f"    schema={repr(self.schema)},\n"
            f"    column_names={repr(self.column_names)}\n"
            ")"
        )


@Operations.register_operation("drop_primary_key")
class DropPrimaryKeyOp(AlterTableOp):
    __slots__: Tuple[str, ...] = ("table_name", "schema", "column_names")

    def __init__(
        self,
        table_name: str,
        schema: Optional[str] = None,
        column_names: Union[Iterator[str], Sequence[str]] = (),
    ) -> None:
        super().__init__(table_name, schema=schema)
        self.column_names: Tuple[str, ...] = tuple(column_names)

    @classmethod
    def drop_primary_key(
        cls,
        operations: Operations,
        table_name: str,
        schema: Optional[str] = None,
        column_names: Union[Iterator[str], Sequence[str]] = (),
    ) -> None:
        operations.invoke(cls(table_name, schema, column_names))

    def reverse(self) -> "AddPrimaryKeyOp":
        return AddPrimaryKeyOp(
            table_name=self.table_name,
            schema=self.schema,
            column_names=self.column_names,
        )

    def to_table(
        self, migration_context: Optional[MigrationContext] = None
    ) -> Table:
        schema_obj: schemaobj.SchemaObjects = schemaobj.SchemaObjects(
            migration_context
        )
        return schema_obj.table(self.table_name, schema=self.schema)

    def to_diff_tuple(self) -> Tuple[str, Table]:
        return "drop_primary_key", self.to_table()

    @classmethod
    def from_constraint(
        cls, primary_key_constraint: PrimaryKeyConstraint
    ) -> "DropPrimaryKeyOp":
        column: Column
        return cls(
            primary_key_constraint.table.name,
            schema=primary_key_constraint.table.schema,
            column_names=(
                column.name for column in primary_key_constraint.columns
            ),
        )

    def __repr__(self) -> str:
        return (
            f"{get_class_qualified_name(type(self))}(\n"
            f"    table_name={repr(self.table_name)},\n"
            f"    schema={repr(self.schema)},\n"
            f"    column_names={repr(self.column_names)}\n"
            ")"
        )


@Operations.implementation_for(AddPrimaryKeyOp)
def add_primary_key(
    operations: Operations, operation: AddPrimaryKeyOp
) -> None:
    operations.execute(  # type: ignore
        AddPrimaryKey(
            operation.table_name,
            schema=operation.schema,
            column_names=operation.column_names,
            bind=operations.get_bind(),
        )
    )


@Operations.implementation_for(DropPrimaryKeyOp)
def drop_primary_key(
    operations: Operations, operation: DropPrimaryKeyOp
) -> None:
    operations.execute(  # type: ignore
        DropPrimaryKey(
            operation.table_name,
            schema=operation.schema,
            bind=operations.get_bind(),
        )
    )
