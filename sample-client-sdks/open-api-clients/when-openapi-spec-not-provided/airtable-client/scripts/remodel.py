import functools
import os
import re
from collections import deque
from itertools import chain, islice
from logging import Logger, getLogger
from pydoc import getdoc
from typing import Any, Callable, Dict, List
from urllib.parse import urljoin
from sob.abc import MarshallableTypes
from sob.model import detect_format, unmarshal
from sob.thesaurus import (
    Thesaurus,
    class_name_from_pointer as _class_name_from_pointer,
)
from sob.utilities import class_name
from sob.utilities.io import read
from airtable_client.client import Client

MODEL_MODULE_PATH: str = os.path.abspath(
    urljoin(
        os.path.abspath(__file__),
        "../airtable_client/model.py",
    )
)
TOKEN_CERBERUS_PATH: str = (
    "app/sustainability/airtable/a.AT.SUSTAINABILITY-personal-access-token"
)
META_BASES_GET_RESPONSE_KEY: str = "meta/bases/get/response"
META_BASES_BASE_ID_TABLES_GET_RESPONSE_KEY: str = (
    "meta/bases/base-id/tables/get/response"
)
BASE_ID_TABLE_GET_RESPONSE_KEY: str = "base-id/table/get/response"
BASE_ID_TABLE_RECORD_ID_GET_RESPONSE_KEY: str = (
    "base-id/table/record-id/get/response"
)

lru_cache: Callable[..., Any] = functools.lru_cache
log: Logger = getLogger(__name__)


def pluralize(noun: str) -> str:
    plural_noun: str = noun
    if not noun.endswith("s"):
        plural_noun = f"{noun}s"
    return plural_noun


def depluralize(noun: str) -> str:
    singular_noun: str = noun
    if pluralize(noun) == noun:
        if noun.endswith("s"):
            singular_noun = noun[:-1]
    return singular_noun


def class_name_from_pointer(pointer: str) -> str:
    """
    This function accepts a JSON pointer and returns an appropriate class
    name for entities found at that pointer

    >>> class_name_from_pointer("meta/bases/get/response#/bases/0")
    Base

    >>> class_name_from_pointer("meta/bases/get/response#/bases")
    Bases

    >>> class_name_from_pointer("meta/bases/get/response#")
    MetaBasesGetResponse

    >>> class_name_from_pointer("meta/bases/base-id/tables/get/response#")
    TablesGetResponse
    """
    name: str = pointer
    if pointer[-1] not in "#/":
        name = pointer.split("#")[-1]
    depluralize_last: bool = bool(
        re.match(r".*/\d+$", name, flags=re.IGNORECASE)
    )
    name_elements: List[str] = re.split(r"/\d+", name, flags=re.IGNORECASE)
    if len(name_elements) > 1:
        name = "/".join(
            filter(
                None,
                chain(
                    map(
                        depluralize,
                        name_elements[: None if depluralize_last else -1],
                    ),
                    () if depluralize_last else name_elements[-1:],
                ),
            )
        )
    name = class_name(name)
    message: str = f"{pointer} -> {name}"
    print(message)
    log.info(message)
    return name


class_name_from_pointer.__doc__ = getdoc(_class_name_from_pointer)


def _clear_record_fields(record: Dict[str, Any]) -> Dict[str, Any]:
    record["fields"].clear()
    return record


class Contractor:
    """
    This class populates a thesaurus of AirTable API response "synonyms",
    organized by endpoint, in order to infer data types and build a data model
    against which our client can validate future API responses
    """

    def __init__(self) -> None:
        self.client: Client = Client(
            bearer_token_cerberus_path=TOKEN_CERBERUS_PATH, echo=True
        )

    @property  # type: ignore
    @lru_cache()
    def thesaurus(self) -> Thesaurus:
        # Create a thesaurus, lookup the bases we have access to,
        # and initialize synonyms for subsequent lookups
        thesaurus: Thesaurus = Thesaurus(
            {
                META_BASES_GET_RESPONSE_KEY: {
                    self.client.request("/meta/bases", method="GET")
                },
                META_BASES_BASE_ID_TABLES_GET_RESPONSE_KEY: set(),
                BASE_ID_TABLE_GET_RESPONSE_KEY: set(),
                BASE_ID_TABLE_RECORD_ID_GET_RESPONSE_KEY: set(),
            }
        )
        # Retrieve the /meta/bases response data from our thesaurus
        meta_bases_get_response: Dict[str, List[Dict[str, str]]] = next(
            iter(thesaurus[META_BASES_GET_RESPONSE_KEY])  # type: ignore
        )
        base_meta: Dict[str, Any]
        tables_meta: Dict[str, Any]
        # Iterate over each base's metadata
        for base_meta in meta_bases_get_response["bases"]:
            base_id: str = base_meta["id"]
            # Get metadata for each table in the base
            tables_response_data: MarshallableTypes = unmarshal(
                detect_format(
                    str(
                        read(  # type: ignore
                            self.client.request(
                                f"/meta/bases/{base_id}/tables", method="GET"
                            )
                        ),
                        encoding="UTF-8",
                    )
                )[0]
            )
            # Add the tables data to our thesaurus
            thesaurus[META_BASES_BASE_ID_TABLES_GET_RESPONSE_KEY].add(
                tables_response_data
            )
            # For each table, lookup records and add them to a set of synonyms
            # in our thesaurus
            for tables_meta in tables_response_data["tables"]:  # type: ignore
                table_id: str = tables_meta["id"]
                # We unmarshal the response data rather than passing along
                # the raw HTTPResponse so that we can manipulate
                # the data before adding it to our synonyms
                response_data: Dict[str, Any] = unmarshal(  # type: ignore
                    detect_format(
                        str(
                            read(  # type: ignore
                                self.client.request(
                                    f"/{base_id}/{table_id}", method="GET"
                                )
                            ),
                            encoding="UTF-8",
                        )
                    )[0]
                )

                def _get_record_id_get_response_data(
                    record: Dict[str, Any]
                ) -> Dict[str, Any]:
                    record_id: str = record["id"]
                    record = unmarshal(  # type: ignore
                        detect_format(
                            str(
                                read(  # type: ignore
                                    self.client.request(
                                        (
                                            f"/{base_id}/{table_id}/"
                                            f"{record_id}"
                                        ),
                                        method="GET",
                                    )
                                ),
                                encoding="UTF-8",
                            )
                        )[0]
                    )
                    return _clear_record_fields(record)  # type: ignore

                # This causes record fields to be interpreted as
                # a generic dictionary rather than a typed object,
                # since the fields will vary by table
                deque(
                    map(_clear_record_fields, response_data["records"]),
                    maxlen=0,
                )
                # Add the modified data to our synonyms
                thesaurus[BASE_ID_TABLE_GET_RESPONSE_KEY].add(response_data)
                # This retrieves response data from individual record lookups
                thesaurus[BASE_ID_TABLE_RECORD_ID_GET_RESPONSE_KEY] |= set(
                    map(
                        _get_record_id_get_response_data,
                        # Limit the number of records we lookup to 10
                        islice(response_data["records"], 10),
                    )
                )
        return thesaurus

    def save(
        self,
        model_path: str = MODEL_MODULE_PATH,
    ) -> None:
        self.thesaurus.save_module(model_path, name=class_name_from_pointer)


def main() -> None:
    Contractor().save()


if __name__ == "__main__":
    main()
