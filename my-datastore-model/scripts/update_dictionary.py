import csv
import os
from collections import OrderedDict
from typing import IO, Dict, Iterable, List, Set, Tuple, Type
from urllib.parse import urljoin

from analytics_orm.declarative import (
    get_base_table_names_subclasses,
    get_class_mapper,
    get_class_schema_name,
)
from analytics_orm.types import Array, Object
from sqlalchemy import Column, ForeignKey  # type: ignore
from sqlalchemy.sql.type_api import TypeEngine  # type: ignore

from my_datastore_orm.base import Base


def _get_path(path: str = "") -> str:
    if not path:
        path = urljoin(os.path.dirname(__file__) + "/", "../dictionary.tsv")
    return path


def read_dictionary(path: str = "") -> Iterable[Dict[str, str]]:
    path = _get_path(path)
    dictionary_io: IO[str]
    dictionary_reader: csv.DictReader
    dictionary_definition: Dict[str, str]
    with open(path) as dictionary_io:
        for dictionary_definition in csv.DictReader(
            dictionary_io, dialect=csv.excel_tab
        ):
            yield dictionary_definition


def write_dictionary(
    definitions: Iterable[Dict[str, str]], path: str = ""
) -> None:
    path = _get_path(path)
    dictionary_io: IO[str]
    definitions = list(definitions)
    if not definitions:
        return
    column_names: Tuple[str, ...] = tuple(definitions[0].keys())
    assert len(column_names) > 3
    with open(path, "w") as dictionary_io:
        dictionary_writer: csv.DictWriter = csv.DictWriter(
            dictionary_io, column_names, dialect=csv.excel_tab
        )
        dictionary_writer.writeheader()
        dictionary_writer.writerows(definitions)


def update_dictionary(path: str = "") -> None:  # noqa: C901
    path = _get_path(path)
    dictionary_definitions: Dict[Tuple[str, str], Dict[str, str]] = (
        OrderedDict(
            [
                (
                    (
                        definition["Table"],
                        definition["Column"],
                    ),
                    definition,
                )
                for definition in read_dictionary(path)
            ]
        )
    )
    column_key: Tuple[str, str]
    column_keys: Set[Tuple[str, str]] = set()
    table_name: str
    snowflake_schema_name: str
    mapping_class: Type["Base"]
    for (
        table_name,
        mapping_class,
    ) in get_base_table_names_subclasses(Base).items():
        column: Column
        snowflake_schema_name = (
            get_class_schema_name(mapping_class, dialect_name="snowflake")
            or ""
        )
        for column in get_class_mapper(mapping_class).columns.values():
            column_name: str = column.name.upper()
            column_type: TypeEngine = column.type
            type_name: str = (
                "ARRAY"
                if isinstance(column_type, Array)
                else (
                    "OBJECT"
                    if isinstance(column_type, Object)
                    else column_type.compile()
                )
            )
            primary_key: str = "Yes" if column.primary_key else "No"
            foreign_keys: List[str] = []
            foreign_key: ForeignKey
            for foreign_key in column.foreign_keys:
                foreign_keys.append(foreign_key.target_fullname)

            foreign_keys.sort()
            repr_foreign_key: str = ", ".join(foreign_keys)
            column_key = (table_name, column_name)
            if column_key in dictionary_definitions:
                if type_name != dictionary_definitions[column_key]["Type"]:
                    print(
                        "Updating column type: "
                        f"{table_name}.{column_name} "
                        f"{dictionary_definitions[column_key]['Type']} "
                        f"-> {type_name}"
                    )
                    dictionary_definitions[column_key]["Type"] = type_name
                if column.comment and (
                    column.comment
                    != dictionary_definitions[column_key]["Comment"]
                ):
                    print(
                        "Updating column comment: "
                        f"{table_name}.{column_name} "
                        f"{dictionary_definitions[column_key]['Comment']} "
                        f"-> {column.comment}"
                    )
                    dictionary_definitions[column_key][
                        "Comment"
                    ] = column.comment
                if (
                    repr_foreign_key
                    != dictionary_definitions[column_key]["Foreign Key"]
                ):
                    print(
                        "Updating foreign key: "
                        f"{table_name}.{column_name} "
                        f"{dictionary_definitions[column_key]['Foreign Key']} "
                        f"-> {repr_foreign_key}"
                    )
                    dictionary_definitions[column_key][
                        "Foreign Key"
                    ] = repr_foreign_key
                if (
                    primary_key
                    != dictionary_definitions[column_key]["Primary Key"]
                ):
                    print(
                        "Updating primary key: "
                        f"{table_name}.{column_name} "
                        f"{dictionary_definitions[column_key]['Primary Key']} "
                        f"-> {primary_key}"
                    )
                    dictionary_definitions[column_key][
                        "Primary Key"
                    ] = primary_key
                if (
                    snowflake_schema_name
                    != dictionary_definitions[column_key]["Snowflake Schema"]
                ):
                    print(
                        "Updating Snowflake schema: "
                        f"{snowflake_schema_name}.{table_name} "
                        f"{dictionary_definitions[column_key]['Snowflake Schema']} "  # noqa
                        f"-> {snowflake_schema_name}"
                    )

                    dictionary_definitions[column_key][
                        "Snowflake Schema"
                    ] = snowflake_schema_name
            else:
                dictionary_definitions[column_key] = OrderedDict(
                    [
                        ("Snowflake Schema", snowflake_schema_name),
                        ("Table", table_name),
                        ("Column", column_name),
                        ("Type", type_name),
                        ("Primary Key", primary_key),
                        ("Foreign Key", repr_foreign_key),
                        ("Comment", column.comment),
                    ]
                )
                print(
                    "Adding column definition: "
                    f"{table_name}.{column_name} {type_name}"
                )
            column_keys.add(column_key)
    for column_key in set(dictionary_definitions.keys()) - column_keys:
        print("Removing column definition: " f'{".".join(column_key)}')
        del dictionary_definitions[column_key]
    write_dictionary(dictionary_definitions.values(), path)


if __name__ == "__main__":
    update_dictionary()
