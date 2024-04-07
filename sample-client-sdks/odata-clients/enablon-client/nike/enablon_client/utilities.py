import inspect
import sob
from functools import lru_cache
from itertools import chain
from typing import (
    TYPE_CHECKING,
    List,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
)
from warnings import warn
from more_itertools import unique_everseen
from sob.utilities.string import camel_split
from .client import Client

__all__: List[str] = [
    "pluralize",
    "depluralize",
    "get_object_class_properties_columns",
    "get_client_method_table_name",
    "get_object_class_table_name",
    "get_client_method_row_class",
]


def _pluralize_last(words: List[str], force: bool = False) -> None:
    """
    Pluralize the last word which is not *already* plural
    """
    word: str
    index: int
    plural_word: str
    for index in range(-1, -len(words) - 1, -1):
        word = words[index]
        plural_word = pluralize(word, force=force)
        if plural_word != word:
            words[index] = plural_word
            break


def pluralize(noun: str, force: bool = False) -> str:
    """
    Given a singular noun, return the plural variation of same
    """
    if len(noun) < 4 and not force:
        # This length restriction prevents operating on acronyms
        return noun
    plural_noun: str = noun
    words: List[str]
    if "_" in noun:
        if noun == "SD_EmissionFactors":
            # This is because there is both an SD_EmissionFactors and
            # SD_EmissionFactor endpoint
            plural_noun = "SD_EmissionsFactors"
        elif noun == "sd_emission_factors":
            # This is because there is both an SD_EmissionFactors and
            # SD_EmissionFactor endpoint
            plural_noun = "sd_emissions_factors"
        else:
            words = noun.split("_")
            if max(map(len, words)) < 4:
                # Since none of the words have more than 3 characters,
                # we'll need to force the last one to be pluralized
                force = True
            _pluralize_last(words, force=force)
            plural_noun = "".join(words)
    else:
        if ("entities" in noun) or ("Entities" in noun):
            plural_noun = noun
        else:
            words = list(camel_split(noun))
            if len(words) > 1:
                _pluralize_last(words)
                plural_noun = "".join(words)
            else:
                if noun.endswith("xis"):
                    plural_noun = f"{noun[:-2]}es"
                elif (
                    noun.endswith("ss")
                    or noun.endswith("us")
                    or noun.endswith("as")
                    or noun.endswith("mcs")
                    or noun.endswith("MCS")
                ):
                    plural_noun = f"{noun}es"
                elif noun.endswith("y"):
                    plural_noun = f"{noun[:-1]}ies"
                elif not noun.endswith("s"):
                    plural_noun = f"{noun}s"
    return plural_noun


def depluralize(noun: str, force: bool = False) -> str:
    """
    Given a plural noun, return the singular variation of same
    """
    if len(noun) < 4 and not force:
        # This length restriction prevents operating on acronyms
        return noun
    words: Sequence[str]
    singular_noun: str = noun
    if "_" in noun:
        if noun == "SD_EmissionFactors":
            # This is because there is both an SD_EmissionFactors and
            # SD_EmissionFactor endpoint
            singular_noun = "SD_EmissionsFactor"
        elif noun == "sd_emission_factors":
            # This is because there is both an SD_EmissionFactors and
            # SD_EmissionFactor endpoint
            singular_noun = "sd_emissions_factor"
        elif noun in (
            "SD_EmissionFactorsAuditTrail_CustomChoice_Mode",
            "sd_emission_factors_audit_trail_custom_choice_mode",
        ):
            # This is because there is both an
            # SD_EmissionFactorsAuditTrail_CustomChoice_Mode and
            # SD_EmissionFactorAuditTrail_CustomChoice_Mode endpoint
            singular_noun = noun
        else:
            words = noun.split("_")
            if max(map(len, words)) < 4:
                # Since none of the words have more than 3 characters,
                # we'll need to force the last one to be pluralized
                force = True
            singular_noun = "_".join(
                chain(
                    map(depluralize, words[:-1]),
                    (depluralize(words[-1], force=force),),
                )
            )
    else:
        words = camel_split(noun)
        if len(words) > 1:
            singular_noun = "".join(map(depluralize, words))
        elif pluralize(noun, force=True) == noun:
            if noun.lower() == "news":
                singular_noun = noun
            elif noun.endswith("xes"):
                singular_noun = f"{noun[:-2]}is"
            elif noun.endswith("ses"):
                singular_noun = noun[:-2]
            elif noun.endswith("ies"):
                singular_noun = f"{noun[:-3]}y"
            elif "Entities" in noun:
                singular_noun = noun.replace("Entities", "Entity")
            elif "entities" in noun:
                singular_noun = noun.replace("entities", "entity")
            elif noun.endswith("s"):
                singular_noun = noun[:-1]
    return singular_noun


@lru_cache()
def get_object_class_properties_columns(
    cls: Type[sob.abc.Object],
    columns: Tuple[str, ...] = (),
) -> Tuple[Tuple[str, str], ...]:
    """
    Return a tuple of tuples where each item is the name of a response
    object property and the column name which should be
    mapped to that property.

    - cls (typing.Type[sob.abc.Object]): An ODATA value item response class.
    - columns((str,)) = (): An (optional) tuple of column names for a target
      table.
    """
    column_name: str
    property_name: str
    properties_columns: List[Tuple[str, str]] = []
    unmapped_columns: Set[str] = set(columns)
    mapped_columns: Set[str] = set()
    property_names: Tuple[str, ...] = sob.meta.read(cls).properties.keys()
    for property_name in property_names:
        column_name = property_name
        if column_name.endswith("_"):
            stripped_column_name: str = column_name.rstrip("_")
            if (stripped_column_name not in property_names) and (
                stripped_column_name not in mapped_columns
            ):
                column_name = stripped_column_name
        if not column_name.endswith("comments"):
            column_name = depluralize(column_name)
        if column_name.endswith("_en"):
            # English is the only language used, and we don't want to include
            # unnecessary metadata in column names
            column_name = column_name[:-3]
        elif (
            column_name.endswith("_fk_id")
            or column_name.endswith("_fk_cs_id")
            or column_name.endswith("_fk_reference")
            or column_name.endswith("_fk_level_no")
            or column_name.endswith("_fk_code")
            or column_name.endswith("_fk_choice_list_eq")
        ):
            # OData properties with foreign-key constraints append "_FK_" + the
            # name of the referenced column/property, however this is not
            # common practice in database column naming, so we strip this
            # metadata from the name.
            column_name = column_name.rpartition("_fk_")[0]
        if "_fk_" in column_name:
            column_name = "_".join(unique_everseen(column_name.split("_fk_")))
        if "key_word" in column_name:
            column_name = column_name.replace("key_word", "keyword")
        if "sub_type" in column_name:
            column_name = column_name.replace("sub_type", "subtype")
        if "entities" in column_name:
            column_name = column_name.replace("entities", "entity")
        if column_name.endswith("_satus"):
            column_name = f"{column_name[:-5]}status"
        if "_satus_" in column_name:
            column_name = column_name.replace("_satus_", "_status_")
        if column_name == "def":
            column_name = "def_"
        if column_name in mapped_columns:
            item: Tuple[str, str]
            preexisting_property_name: str = dict(
                reversed(item) for item in properties_columns  # type: ignore
            )[
                column_name  # type: ignore
            ]
            raise KeyError(
                f'The column/property "{column_name}" was encountered twice, '
                f'for both "{property_name}" and "{preexisting_property_name}"'
            )
        if columns:
            # This ensures the column name actually maps to one of the
            # specified columns, if column names were provided
            try:
                unmapped_columns.remove(column_name)
            except KeyError:
                warn(f'"{column_name}" not in {repr(columns)}')
                continue
        mapped_columns.add(column_name)
        # Store the OData property -> ORM column mapping
        properties_columns.append((property_name, column_name))
    return tuple(properties_columns)


@lru_cache()
def get_client_method_table_name(method_name: str) -> str:
    return depluralize(
        method_name.replace("key_word", "keyword")
        .replace("sub_type", "subtype")
        .replace("entities", "entity")
    ).upper()


@lru_cache()
def get_object_class_table_name(cls: Type[sob.abc.Object]) -> str:
    return get_client_method_table_name(
        sob.utilities.string.property_name(cls.__name__)
    )


@lru_cache()
def get_service_root_table_name(name: str) -> str:
    """
    Given the name of an ODATA service root, return a table name.
    """
    return get_client_method_table_name(
        sob.utilities.string.property_name(name)
    )


@lru_cache()
def get_client_method_row_class(name: str) -> Type[sob.abc.Object]:
    """
    Given the name of a client method, return the class
    representing rows in the response value.

    Parameters:

    - name (str): The name of a method of `nike.enablon_client.client.Client`
    """
    response_class: Type[sob.abc.Object] = inspect.signature(
        getattr(Client, name)
    ).return_annotation.__args__[0]
    response_meta: Optional[sob.abc.ObjectMeta] = sob.meta.object_read(
        response_class
    )
    if TYPE_CHECKING:
        assert response_meta is not None
    response_properties: Optional[
        sob.abc.Properties
    ] = response_meta.properties
    if TYPE_CHECKING:
        assert response_properties is not None
    value_types: Optional[sob.abc.Types] = response_properties["value"].types
    if TYPE_CHECKING:
        assert value_types is not None
    value_class: Union[type, sob.abc.Property] = value_types[0]
    if TYPE_CHECKING:
        assert isinstance(value_class, type) and issubclass(
            value_class, sob.abc.Array
        )
    value_meta: Optional[sob.abc.ArrayMeta] = sob.meta.array_read(value_class)
    if TYPE_CHECKING:
        assert value_meta is not None
    item_types: Optional[sob.abc.Types] = value_meta.item_types
    if TYPE_CHECKING:
        assert item_types is not None
    row_class: Union[type, sob.abc.Property] = item_types[0]
    if TYPE_CHECKING:
        assert isinstance(row_class, type) and issubclass(
            row_class, sob.abc.Object
        )
    return row_class
