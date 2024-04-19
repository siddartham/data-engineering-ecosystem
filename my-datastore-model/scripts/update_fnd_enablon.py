import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from functools import lru_cache
from pathlib import Path
from subprocess import check_call
from typing import (
    TYPE_CHECKING,
    Dict,
    Iterable,
    List,
    Literal,
    Match,
    Optional,
    Pattern,
    Set,
    Tuple,
    Type,
    Union,
)
from warnings import warn
from xml.etree.ElementTree import XML, Element

import sob
from enablon_client.client import Client
from enablon_client.model import ServiceRoot, ServiceRootResponse
from enablon_client.utilities import (
    get_client_method_row_class,
    get_object_class_properties_columns,
    get_service_root_table_name,
)

NAMESPACES: Dict[str, str] = {
    "edmx": "http://docs.oasis-open.org/odata/ns/edmx",
    "edm": "http://docs.oasis-open.org/odata/ns/edm",
}
SQLALCHEMY_TYPE_MAPPING: Dict[str, str] = {
    "Edm.Int32": "Integer",
    "Edm.String": "String",
    "Edm.Double": "Float",
    "Edm.DateTimeOffset": "DateTime",
    "Edm.Byte": "Integer",
}
TYPE_MAPPING: Dict[str, str] = {
    "Edm.Int32": "int",
    "Edm.String": "str",
    "Edm.Double": "float",
    "Edm.DateTimeOffset": "datetime.datetime",
    "Edm.Byte": "int",
}
SOB_TYPE_MAPPING: Dict[type, str] = {
    sob.properties.Date: "Date",
    date: "Date",
}
FND_ENABLON_PATH: Path = (
    Path(__file__)
    .absolute()
    .parent.parent.joinpath("my_datastore_model", "fnd_enablon.py")
)


@lru_cache()
def get_client() -> Client:
    return Client(
        url_cerberus_path="app/org/enablon/url-prod",
        user_cerberus_path="app/org/enablon/user-prod",
        password_cerberus_path=("app/org/enablon/password-prod"),
        echo=False,
    )


@lru_cache()
def get_metadata() -> Element:
    client: Client = get_client()
    return XML(client.metadata.read())  # type: ignore


def iter_service_root_row_properties_columns_types(
    name: str,
) -> Iterable[Tuple[str, Tuple[str, str]]]:
    """
    Given the name of an ODATA service root, yield a 2-part tuple of
    the JSON property name (not the python class property name) and the
    corresponding column name in the target table.
    """
    cls: Type[sob.abc.Object] = get_client_method_row_class(
        sob.utilities.string.property_name(name)
    )
    meta: Optional[sob.abc.ObjectMeta] = sob.meta.object_read(cls)
    if TYPE_CHECKING:
        assert meta
    properties: Optional[sob.abc.Properties] = meta.properties
    if TYPE_CHECKING:
        assert properties
    property_name: str
    column_name: str
    for property_name, column_name in get_object_class_properties_columns(cls):
        property: sob.abc.Property = properties[property_name]
        property_type: Union[sob.abc.Property, type, Literal[""]] = (
            property.types[0] if property.types else ""  # type: ignore
        )
        if property_type and not isinstance(property_type, type):
            property_type = type(property_type)
        column_type: str = ""
        if isinstance(property_type, type):
            column_type = SOB_TYPE_MAPPING.get(property_type, "")
        yield (property.name or property_name, (column_name, column_type))


def get_entity_type(name: str) -> Element:
    """
    Get the XML element describing an entity type
    """
    entity_type: Optional[Element] = get_metadata().find(
        (
            ".//edmx:DataServices"
            "/edm:Schema[@Namespace='Enablon']"
            f"/edm:EntityType[@Name='{name}']"
        ),
        namespaces=NAMESPACES,
    )
    if entity_type is None:
        raise ValueError(
            f'No entity type "{name}" found in the Enablon metadata'
        )
    return entity_type


def iter_entity_type_key(entity_type: Element) -> Iterable[str]:
    key: Optional[Element] = entity_type.find("edm:Key", namespaces=NAMESPACES)
    if key is not None:
        property_ref: Element
        for property_ref in key.findall(
            "edm:PropertyRef", namespaces=NAMESPACES
        ):
            yield property_ref.attrib["Name"]


def iter_navigation_property_referential_constraints(
    navigation_property: Element,
) -> Iterable[Element]:
    referential_constraint: Element
    yield from navigation_property.findall(
        "edm:ReferentialConstraint", namespaces=NAMESPACES
    )


@dataclass
class EntityTypeProperty:
    entity_type: str
    property: str


@dataclass
class PropertiesReferences:
    property_names: List[str] = field(default_factory=list)
    reference_entity_types_properties: List[EntityTypeProperty] = field(
        default_factory=list
    )


def iter_entity_type_properties_references(
    entity_type: Element,
) -> Iterable[PropertiesReferences]:
    navigation_property: Element
    for navigation_property in entity_type.findall(
        "edm:NavigationProperty", namespaces=NAMESPACES
    ):
        referenced_entity_type: str = navigation_property.attrib[
            "Type"
        ].rpartition(".")[-1]
        properties_references: PropertiesReferences = PropertiesReferences()
        referential_constraint: Element
        for (
            referential_constraint
        ) in iter_navigation_property_referential_constraints(
            navigation_property
        ):
            properties_references.property_names.append(
                referential_constraint.attrib["Property"]
            )
            properties_references.reference_entity_types_properties.append(
                EntityTypeProperty(
                    entity_type=referenced_entity_type,
                    property=referential_constraint.attrib[
                        "ReferencedProperty"
                    ],
                )
            )
        yield properties_references


def iter_service_root_table_class_source(  # noqa: C901
    source: str,
    service_root: str,
    table_name: str = "",
    class_name: str = "",
) -> Iterable[str]:
    try:
        properties_columns_types: Dict[str, Tuple[str, str]] = dict(
            iter_service_root_row_properties_columns_types(service_root)
        )
    except AttributeError:
        warn(
            f'The service root "{service_root}" cannot be added, it is either '
            "empty, or the `enablon-client` package needs "
            "remodeled/updated."
        )
        return
    if not table_name:
        table_name = get_service_root_table_name(service_root)
    if not class_name:
        service_roots_classes: Dict[str, str] = (
            get_source_service_roots_classes(source)
        )
        try:
            class_name = service_roots_classes[service_root]
        except KeyError:
            class_name = sob.utilities.string.class_name(table_name)
    yield ""
    yield ""
    yield f"class {class_name}(Base):"
    entity_type: Element = get_entity_type(service_root)
    key: Tuple[str, ...] = tuple(iter_entity_type_key(entity_type))
    if not key:
        raise ValueError(f"No primary key found for {service_root}")
    docstring: List[str] = [
        '    """',
        f"    {table_name}",
        "",
        "    Primary Key:",
        "",
    ]
    boolean_properties: Set[str] = set()
    inline_properties_foreign_keys: Dict[str, str] = {}
    foreign_key_constraints: List[str] = []
    foreign_key_docstrings: Dict[str, str] = {}
    properties_references: PropertiesReferences
    reference_class_name: str
    reference_table_name: str
    reference_properties_columns_types: Dict[str, Tuple[str, str]]
    reference_entity_type_property: EntityTypeProperty
    property_name: str
    reference_property_name: str
    for properties_references in iter_entity_type_properties_references(
        entity_type=entity_type
    ):
        if not properties_references.property_names:
            continue
        reference_entity_type_property = (
            properties_references.reference_entity_types_properties[0]
        )
        if reference_entity_type_property.entity_type == "No_Yes":
            boolean_properties.add(properties_references.property_names[0])
        else:
            columns_representation: str = sob.utilities.string.indent(
                sob.utilities.inspect.represent(
                    tuple(
                        map(
                            lambda entity_type_property_name: (
                                properties_columns_types[
                                    entity_type_property_name
                                ][0].upper()
                            ),
                            properties_references.property_names,
                        )
                    )
                )
            )
            reference_table_exists: bool = False
            reference_columns_lines: List[str] = ["("]
            for (
                reference_entity_type_property
            ) in properties_references.reference_entity_types_properties:
                try:
                    reference_properties_columns_types = dict(
                        iter_service_root_row_properties_columns_types(
                            reference_entity_type_property.entity_type
                        )
                    )
                except AttributeError:
                    # The referenced table is empty or missing
                    continue
                try:
                    reference_table_name = get_service_root_table_name(
                        reference_entity_type_property.entity_type
                    )
                    reference_class_name = get_source_tables_classes(source)[
                        reference_table_name.upper()
                    ]
                except KeyError:
                    reference_table_exists = False
                    break
                reference_property_name = reference_properties_columns_types[
                    reference_entity_type_property.property
                ][0]
                reference_columns_lines.append(
                    f"        {reference_class_name}"
                    f".{reference_property_name},"
                )
                # Docstring
                for property_name, reference_property_name in zip(
                    properties_references.property_names,
                    reference_properties_columns_types[
                        reference_entity_type_property.property
                    ],
                ):
                    foreign_key_docstrings[property_name] = (
                        f" -> {reference_table_name}"
                        f".{reference_property_name.upper()}"
                    )
                reference_table_exists = True
            if not reference_table_exists:
                continue
            reference_columns_lines.append("    )")
            reference_columns_representation: str = "\n".join(
                reference_columns_lines
            )
            foreign_key_constraints.append(
                "ForeignKeyConstraint(\n"
                f"    columns={columns_representation},\n"
                f"    refcolumns={reference_columns_representation},\n"
                f"    table={class_name}.__table__,    # noqa\n"
                f"    use_alter=True,\n"
                ")"
            )
    columns: List[str] = []
    previous_column_is_in_primary_key: bool = True
    property: Element
    for property in sorted(
        entity_type.findall("edm:Property", namespaces=NAMESPACES),
        key=lambda property: property.attrib["Name"] in key,
        reverse=True,
    ):
        entity_type_property_name: str = property.attrib["Name"]
        entity_type_property_type: str = property.attrib["Type"]
        is_in_primary_key: bool = bool(entity_type_property_name in key)
        if previous_column_is_in_primary_key and not is_in_primary_key:
            docstring += [
                "",
                "    Other Columns/Properties:",
                "",
            ]
            previous_column_is_in_primary_key = False
        entity_type_property_nullable: bool = (
            property.attrib.get("Nullable", "true") == "true"
        )
        class_property_name: str
        sqlalchemy_type_name: str
        class_property_name, sqlalchemy_type_name = properties_columns_types[
            entity_type_property_name
        ]
        type_name: str
        if entity_type_property_name in boolean_properties:
            type_name = "bool"
            sqlalchemy_type_name = "Boolean"
        else:
            type_name = TYPE_MAPPING[entity_type_property_type]
            if not sqlalchemy_type_name:
                sqlalchemy_type_name = SQLALCHEMY_TYPE_MAPPING[
                    entity_type_property_type
                ]
        column_name: str = class_property_name.upper()
        foreign_key_docstring: str = foreign_key_docstrings.get(
            entity_type_property_name, ""
        )
        docstring_line: str = (
            f"    - {class_property_name} ({type_name}){foreign_key_docstring}"
        )
        if (
            foreign_key_docstring
            and len(docstring_line) > sob.utilities.string.MAX_LINE_LENGTH
        ):
            docstring_line = (
                f"    - {class_property_name} ({type_name})"
                f"\n     {foreign_key_docstring}"
            )
        docstring.append(docstring_line)
        primary_key_source: str = (
            "        primary_key=True,\n" if is_in_primary_key else ""
        )
        autoincrement_source: str = (
            "        autoincrement=False,\n"
            if len(key) == 1 and is_in_primary_key
            else ""
        )
        foreign_key_source: str = inline_properties_foreign_keys.get(
            entity_type_property_name, ""
        )
        nullable_source: str = (
            ""
            if (
                (is_in_primary_key and not entity_type_property_nullable)
                or (entity_type_property_nullable and not is_in_primary_key)
            )
            else (
                "        nullable=True,\n"
                if is_in_primary_key and entity_type_property_nullable
                else "        nullable=False,\n"
            )
        )
        columns.append(
            f"    {class_property_name} = Column(\n"
            f'        "{column_name}",\n'
            f"        {sqlalchemy_type_name},\n"
            f"{foreign_key_source}"
            f"{primary_key_source}"
            f"{autoincrement_source}"
            f"{nullable_source}"
            "    )"
        )
    docstring += ['    """']
    yield from docstring
    yield ""
    yield from columns
    yield ""
    yield ""
    yield from foreign_key_constraints


def get_service_root_class_source(
    source: str, service_root: str, table_name: str = "", class_name: str = ""
) -> Tuple[str, str]:
    return (
        "\n".join(
            iter_service_root_table_class_source(
                source, service_root, table_name, class_name
            )
        )
    ).partition("\n\n\n")[::2]


def iter_service_root_names() -> Iterable[str]:
    client: Client = get_client()
    service_root_response: ServiceRootResponse = client.get()
    assert service_root_response.value
    service_root: ServiceRoot
    for service_root in service_root_response.value:
        if service_root.name:
            yield service_root.name


@lru_cache()
def get_service_root_names() -> Tuple[str, ...]:
    return tuple(iter_service_root_names())


def iter_source_classes_service_roots(
    source: str,
) -> Iterable[Tuple[str, str]]:
    service_root_name: str
    source_tables_classes: Dict[str, str] = get_source_tables_classes(source)
    for service_root_name in get_service_root_names():
        try:
            yield source_tables_classes[
                get_service_root_table_name(service_root_name).upper()
            ], service_root_name
        except KeyError:
            pass


@lru_cache()
def get_source_classes_service_roots(source: str) -> Dict[str, str]:
    return dict(iter_source_classes_service_roots(source))


@lru_cache()
def get_source_service_roots_classes(source: str) -> Dict[str, str]:
    key: str
    value: str
    return {
        value: key
        for key, value in get_source_classes_service_roots(source).items()
    }


_SOURCE_CLASS_NAME_PATTERN: Pattern = re.compile(
    r"\nclass\s+([^\(\s)]+)\s*\([^\)]*Base[^\)]*\)\:"
    r"(?:.|\n)+?"
    r"(?=\nclass\s+(?:[^\(\s)]+)\s*\([^\)]*Base[^\)]*\)\:|$)",
    re.MULTILINE,
)


def iter_source_tables_classes(source: str) -> Iterable[Tuple[str, str]]:
    class_name: str
    for class_name in _SOURCE_CLASS_NAME_PATTERN.findall(source):
        table_name: str = sob.utilities.string.property_name(
            class_name
        ).upper()
        yield (
            table_name,
            class_name,
        )


@lru_cache()
def get_source_tables_classes(source: str) -> Dict[str, str]:
    return dict(iter_source_tables_classes(source))


def iter_source_service_roots_classes(
    source: str,
) -> Iterable[Tuple[str, str]]:
    classes_service_roots: Dict[str, str] = get_source_classes_service_roots(
        source
    )
    class_name: str
    for class_name in get_source_tables_classes(source).values():
        if class_name in classes_service_roots:
            yield classes_service_roots[class_name], class_name


def get_module_source() -> str:
    with open(FND_ENABLON_PATH, "r") as source_io:
        return source_io.read()


@lru_cache()
def get_class_pattern(name: str) -> Pattern:
    return re.compile(
        r"\nclass\s+"
        f"{name}"
        r"\s*\([^\)]*Base[^\)]*\)\:"
        r"(?:.|\n)+?"
        r"(?=\nclass\s*(?:[^\(\s)]+)\s*\([^\)]*Base[^\)]*\)\:|$|\n#)",
    )


FOREIGN_KEY_SEPARATOR: str = "\n\n# Foreign Keys\n"


def update_source_service_root(
    source: str, service_root: str, class_name: str = ""
) -> str:
    table_name: str
    table_name = get_service_root_table_name(service_root)
    try:
        class_name = get_source_tables_classes(source)[table_name]
    except KeyError:
        warn(table_name)
        return source
    pattern: Pattern = get_class_pattern(class_name)
    match: Optional[Match] = pattern.search(source)
    if not match:
        raise ValueError(f"No match found for {class_name}")
    class_source: str
    foreign_key_source: str
    class_source, foreign_key_source = get_service_root_class_source(
        source, service_root, table_name, class_name
    )
    source = pattern.sub(
        f"{class_source}\n\n",
        source,
    )
    source = f"{source.rstrip()}\n{foreign_key_source}\n"
    return source


def get_updated_module_source(
    add_service_roots: Iterable[str] = (), dry_run: bool = False
) -> str:
    if isinstance(add_service_roots, str):
        add_service_roots = (add_service_roots,)
    service_root_names: Tuple[str, ...] = get_service_root_names()
    service_root: str
    invalid_service_root_names: Tuple[str, ...] = tuple(
        filter(
            lambda service_root: service_root not in service_root_names,
            add_service_roots,
        )
    )
    if invalid_service_root_names:
        warn(
            "Invalid Service Roots:\n{}".format(
                "\n".join(invalid_service_root_names)
            )
        )
        add_service_roots = tuple(
            filter(
                lambda service_root: service_root in service_root_names,
                add_service_roots,
            )
        )
    source: str = get_module_source()
    source = source.partition(FOREIGN_KEY_SEPARATOR)[0]
    source = f"{source.rstrip()}\n{FOREIGN_KEY_SEPARATOR}"
    assert FOREIGN_KEY_SEPARATOR in source
    # Update existing classes
    existing_service_roots: Set[str] = set()
    class_name: str
    for service_root, class_name in iter_source_service_roots_classes(source):
        source = update_source_service_root(source, service_root, class_name)
        existing_service_roots.add(service_root)
    foreign_keys_source: str
    source, foreign_keys_source = source.partition(FOREIGN_KEY_SEPARATOR)[::2]
    if not foreign_keys_source:
        raise RuntimeError("No Foreign Keys found!")
    # Add service roots
    for service_root in add_service_roots:
        if service_root in existing_service_roots:
            warn(f'The service root "{service_root}" has already been added.')
            continue
        service_root_source: str
        foreign_key_source: str
        (
            service_root_source,
            foreign_key_source,
        ) = get_service_root_class_source(source, service_root)
        source = f"{source.rstrip()}\n\n{service_root_source}\n"
        if foreign_key_source:
            foreign_keys_source = (
                f"{foreign_keys_source.rstrip()}\n{foreign_key_source}\n"
            )
    return f"{source}{FOREIGN_KEY_SEPARATOR}{foreign_keys_source}"


def update_module_source(
    add_service_roots: Iterable[str] = (), dry_run: bool = False
) -> None:
    source: str = get_updated_module_source(
        add_service_roots=add_service_roots
    )
    source = sob.utilities.string.suffix_long_lines(source)
    if dry_run:
        print(source)
    else:
        with open(FND_ENABLON_PATH, "w") as source_io:
            source_io.write(source)
        check_call([sys.executable, "-m", "black", str(FND_ENABLON_PATH)])


def main() -> None:
    parser = argparse.ArgumentParser("python3 scripts/update_fnd_enablon.py")
    parser.add_argument(
        "--add-service-root",
        "-asr",
        action="append",
        help=(
            "The name of one or more Enablon OData Blink API service roots "
            "for which to generate and append a new ORM class"
        ),
    )
    parser.add_argument(
        "--dry-run",
        "-dr",
        action="store_true",
        help=(
            "This flag will cause the new classes to be printed, but "
            "no changes will be made to the module"
        ),
    )
    namespace: argparse.Namespace = parser.parse_args()
    update_module_source(
        add_service_roots=namespace.add_service_root or (),
        dry_run=namespace.dry_run,
    )


if __name__ == "__main__":
    main()
