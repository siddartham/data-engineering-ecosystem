import sob
import argparse
import functools
import json
import re
import sys
import os
from datetime import datetime
from pathlib import Path
from subprocess import check_call
from pydoc import getdoc
from typing import (
    Any,
    Callable,
    Dict,
    IO,
    List,
    Optional,
    OrderedDict,
    Iterable,
)
from sob.abc import MarshallableTypes, Readable
from sob.model import Dictionary, detect_format, unmarshal
from sob.thesaurus import (
    Thesaurus,
    class_name_from_pointer as _class_name_from_pointer,
)
from sob.utilities.io import read
from sob.utilities.string import class_name, property_name, suffix_long_lines
from sob.utilities.types import NULL
from nike.enablon_client.model import ServiceRootResponse, ServiceRoot
from nike.enablon_client.client import Client
from nike.enablon_client.utilities import depluralize, pluralize

_HAND_WRITTEN_CODE_RE = (
    r"((?:.|\n)*?\n[ ][ ][ ][ ]def[ ]+get(?:.|\n)*?)"
    r"(?=(?:(?:\n[ ][ ][ ][ ]def[ ](?:.|\n)*$)|(?:[\s]*$)))"
)
TOP: int = 100
PROJECT_DIRECTORY_PATH: Path = Path(__file__).absolute().parent.parent
MODEL_MODULE_PATH: Path = PROJECT_DIRECTORY_PATH.joinpath(
    "nike", "enablon_client", "model.py"
)
CLIENT_MODULE_PATH: Path = PROJECT_DIRECTORY_PATH.joinpath(
    "nike", "enablon_client", "client.py"
)
METADATA_PATH: Path = PROJECT_DIRECTORY_PATH.joinpath("metadata.xml")
SERVICE_ROOT_PATH: Path = PROJECT_DIRECTORY_PATH.joinpath("service-root.json")
TEMP_SERVICE_ROOT_PATH: Path = PROJECT_DIRECTORY_PATH.joinpath(
    ".service-root.json"
)
lru_cache: Callable[..., Any] = functools.lru_cache


def is_datetime_field(name: str) -> bool:
    return "ModifiedOn" in name or "CreatedOn" in name


def class_name_from_pointer(pointer: str) -> str:
    name: str = pointer
    if pointer.endswith("#/value/0"):
        name = class_name(depluralize(name[:-9]))
    elif pointer.endswith("#/value"):
        name = pluralize(name[:-7])
    elif "/" not in name:
        name = "{}/response".format(name.rstrip("#"))
    name = _class_name_from_pointer(name)
    print(f"{pointer} -> {name} (JSON pointer -> class name)")
    return name


class_name_from_pointer.__doc__ = getdoc(_class_name_from_pointer)


def iter_service_root_response_item_class_names(
    service_root_response: ServiceRootResponse,
) -> Iterable[str]:
    assert service_root_response.value
    name: str
    service_root: ServiceRoot
    yield from map(
        lambda name: class_name_from_pointer(f"{name}#/value/0"),
        filter(
            None,
            map(
                lambda service_root: service_root.name,
                service_root_response.value,
            ),
        ),
    )


class Contractor:
    def __init__(self) -> None:
        self.client: Client = Client(
            url_cerberus_path="app/sustainability/enablon/url-prod",
            user_cerberus_path="app/sustainability/enablon/user-prod",
            password_cerberus_path=(
                "app/sustainability/enablon/password-prod"
            ),
            echo=False,
        )

    def get_service_root(self) -> Readable:
        return self.client.request("/", method="GET")

    @property  # type: ignore
    @lru_cache()
    def thesaurus(self) -> Thesaurus:
        thesaurus: Thesaurus = Thesaurus(
            {"service-root": [self.get_service_root()]}
        )
        service_root: MarshallableTypes = next(iter(thesaurus["service-root"]))
        assert isinstance(service_root, Dictionary)
        service: Dictionary
        for service in service_root["value"]:
            if service["kind"] == "EntitySet":
                empty: bool = False
                key: str
                value: Any
                row: Dict[str, Any]
                url: str = f'/{service["url"]}?$count=true'
                if TOP:
                    url = f"{url}&top={TOP}"
                filtered_url: str = url
                unused_fields: Optional[List[str]] = None
                unused_datetime_fields: Optional[List[str]] = None
                list(filter(is_datetime_field, unused_fields or ()))
                while filtered_url:
                    response: Readable = self.client.request(
                        filtered_url, method="GET"
                    )
                    data: Dict[str, Any] = unmarshal(  # type: ignore
                        detect_format(
                            str(
                                read(response),  # type: ignore
                                encoding="utf-8",
                            )
                        )[0]
                    )
                    if (url == filtered_url) and not data["value"]:
                        # There is no data for this endpoint
                        empty = True
                        break
                    if (unused_fields is None) or unused_fields:
                        for row in data["value"]:
                            if unused_fields is None:
                                unused_fields = list(row.keys())
                            if unused_datetime_fields is None:
                                unused_datetime_fields = list(
                                    filter(is_datetime_field, unused_fields)
                                )
                            for key, value in row.items():
                                if (value is not None) and (value is not NULL):
                                    if key in unused_datetime_fields:
                                        unused_datetime_fields.remove(key)
                                    if key in unused_fields:
                                        unused_fields.remove(key)
                                        if not unused_fields:
                                            break
                            if not unused_fields:
                                break
                        if unused_fields:
                            filtered_url = (
                                f"{url}&$filter="
                                f"{unused_fields.pop(0)}%20ne%20null"
                            )
                        else:
                            filtered_url = ""
                    else:
                        filtered_url = ""
                    if "@odata.nextLink" not in data:
                        data["@odata.nextLink"] = "*"
                    thesaurus[service["name"]].add(data)
                if unused_datetime_fields and not empty:
                    # Make sure all "ModifiedOn" and "CreatedOn"
                    # fields are typed correctly
                    thesaurus[service["name"]].add(
                        sob.model.Dictionary(
                            {
                                "value": [
                                    {
                                        key: datetime.now().isoformat()
                                        for key in unused_datetime_fields
                                    },
                                ]
                            }
                        )
                    )
        return thesaurus

    def get_client_source(self, client_path: Path = CLIENT_MODULE_PATH) -> str:
        client_source_io: IO[str]
        with open(client_path, "r") as client_source_io:
            source: str = client_source_io.read()
        lines: List[str] = [
            re.match(_HAND_WRITTEN_CODE_RE, source)  # type: ignore
            .group()
            .rstrip()
        ]
        service_root: Dictionary = next(iter(self.thesaurus["service-root"]))
        service: Dictionary
        for service in service_root["value"]:
            if service["kind"] == "EntitySet":
                if service["name"] not in self.thesaurus:
                    # There was no data for this endpoint
                    continue
                service_url: str = service["url"]
                method_name: str = property_name(service["name"])
                response_class_name: str = "model.{}".format(
                    class_name_from_pointer(service["name"])
                )
                lines.append(
                    f"\n"
                    f"    def {method_name}(\n"
                    f"        self,\n"
                    f"        filter: str = '',\n"
                    f"        orderby: str = '',\n"
                    f"        top: int = 0,\n"
                    f"        skip: int = 0\n"
                    f"    ) -> Iterable[{response_class_name}]:\n"
                    f"        response_instance: {response_class_name}\n"
                    f"        filter_query_argument: str = (\n"
                    "            f'&$filter={quote(filter)}'\n"
                    "            if filter else\n"
                    "            ''\n"
                    f"        )\n"
                    f"        orderby_query_argument: str = (\n"
                    "            f'&$orderby={quote(orderby)}'\n"
                    "            if orderby else\n"
                    "            ''\n"
                    f"        )\n"
                    f"        top_query_argument: str = (\n"
                    "            f'&$top={top}'\n"
                    "            if top else\n"
                    "            ''\n"
                    f"        )\n"
                    f"        skip_query_argument: str = (\n"
                    "            f'&skip={skip}'\n"
                    "            if skip else\n"
                    "            ''\n"
                    f"        )\n"
                    f"        url: Optional[str] = (\n"
                    f"            '/{service_url}?'\n"
                    f"            '$count=true'\n"
                    "            f'{filter_query_argument}'\n"
                    "            f'{orderby_query_argument}'\n"
                    "            f'{top_query_argument}'\n"
                    "            f'{skip_query_argument}'\n"
                    f"        )\n"
                    f"        while url:\n"
                    f"            response_instance = ("
                    f"                {response_class_name}(\n"
                    f"                    self.request(\n"
                    f"                        url,\n"
                    f"                        method='GET'\n"
                    f"                    )\n"
                    f"                )\n"
                    f"            )\n"
                    f"            yield response_instance\n"
                    f"            url = response_instance.odata_next_link"
                )
        return "\n".join(lines + [""])

    def save_model(self, model_path: Path = MODEL_MODULE_PATH) -> None:
        self.thesaurus.save_module(
            str(model_path), name=class_name_from_pointer
        )

    def save_client(self, client_path: Path = CLIENT_MODULE_PATH) -> None:
        source: str = self.get_client_source(client_path)
        with open(client_path, "w") as client_io:
            client_io.write(source)
        check_call((sys.executable, "-m", "black", client_path))
        with open(client_path, "r") as client_io:
            source = client_io.read()
        suffixed_source: str = suffix_long_lines(source)
        if suffixed_source != source:
            with open(client_path, "w") as client_io:
                client_io.write(suffixed_source)

    def save_metadata(self) -> bool:
        """
        Save a local copy of this APIs metadata and return `True` if the
        metadata has changed or `False` if nothing has changed.
        """
        metadata: str = self.client.metadata.read()  # type: ignore
        changed: bool
        try:
            with open(METADATA_PATH, "r") as metadata_io:
                changed = bool(metadata_io.read() != metadata)
        except FileNotFoundError:
            changed = True
        if changed:
            with open(METADATA_PATH, "w") as metadata_io:
                metadata_io.write(metadata)
        return changed

    def save_temp_service_root(self) -> bool:
        """
        Save a local copy of this APIs service root and return `True` if the
        data has changed or `False` if nothing has changed.
        """
        service_root: str = json.dumps(
            json.load(
                self.get_service_root(),
                object_hook=OrderedDict,
            ),
            indent=4,
        )
        changed: bool
        try:
            with open(SERVICE_ROOT_PATH, "r") as service_root_io:
                changed = bool(service_root_io.read() != service_root)
        except FileNotFoundError:
            changed = True
        if changed:
            with open(TEMP_SERVICE_ROOT_PATH, "w") as service_root_io:
                service_root_io.write(service_root)
        return changed

    def save(
        self,
        force: bool = False,
    ) -> None:
        """
        Recreate the modules `nike.enablon_client.client` and
        `nike.enablon_client.model` if metadata has changed since the last
        time we remodeled, or if `force==True`.
        """
        if self.save_metadata() or self.save_temp_service_root() or force:
            self.save_model()
            self.save_client()
            if TEMP_SERVICE_ROOT_PATH.is_file():
                self.print_new_tables()
                os.remove(SERVICE_ROOT_PATH)
                TEMP_SERVICE_ROOT_PATH.rename(SERVICE_ROOT_PATH)

    def print_new_tables(self) -> None:
        """
        Print a markdown-formatted table class and table name for all new
        tables
        """
        old_service_root: ServiceRootResponse
        with open(SERVICE_ROOT_PATH, "r") as service_root_io:
            assert isinstance(service_root_io, Readable)
            old_service_root = ServiceRootResponse(service_root_io)
        with open(TEMP_SERVICE_ROOT_PATH, "r") as service_root_io:
            assert isinstance(service_root_io, Readable)
            new_service_root = ServiceRootResponse(service_root_io)
        name: str
        print("|| Class Name || Table Name ||")
        for name in sorted(
            set(iter_service_root_response_item_class_names(old_service_root))
            - set(
                iter_service_root_response_item_class_names(new_service_root)
            )
        ):
            print(
                f"| nike.enablon_client.model.{name} | "
                f"{property_name(name).upper()} |"
            )


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Force remodeling, even if metadata has not changed",
    )
    namespace: argparse.Namespace = parser.parse_args()
    Contractor().save(force=namespace.force)


if __name__ == "__main__":
    main()
