import functools
import os
from pydoc import getdoc
from subprocess import getstatusoutput
from typing import Any, Callable, Dict, List, Optional
from urllib.error import HTTPError
from urllib.parse import urljoin
from xml.dom import minidom  # noqa

from sob.thesaurus import Synonyms, Thesaurus
from sob.thesaurus import class_name_from_pointer as _class_name_from_pointer
from sob.utilities import class_name

from map_airflow_client.experimental.client import Client

MODEL_MODULE_PATH: str = os.path.abspath(
    urljoin(
        os.path.abspath(__file__),
        "../map_airflow_client/experimental/model.py",
    )
)

thesaurus_lru_cache: Callable[
    [int, bool], Callable[..., Thesaurus]
] = functools.lru_cache  # type: ignore


def run(command: str) -> str:
    print(command)
    status, output = getstatusoutput(command)
    # Create an error if a non-zero exit status is encountered
    if status:
        raise OSError(output)
    else:
        print(output)
    return output


def pluralize(noun: str) -> str:
    plural_noun: str = noun
    if "Entities" in noun:
        plural_noun = noun
    elif noun.endswith("xis"):
        plural_noun = f"{noun[:-2]}es"
    elif noun.endswith("ss"):
        plural_noun = f"{noun}es"
    elif noun.endswith("y"):
        plural_noun = f"{noun[:-1]}ies"
    elif not noun.endswith("s"):
        plural_noun = f"{noun}s"
    return plural_noun


def depluralize(noun: str) -> str:
    singular_noun: str = noun
    if pluralize(noun) == noun:
        if noun.endswith("xes"):
            singular_noun = f"{noun[:-2]}is"
        elif noun.endswith("ses"):
            singular_noun = noun[:-2]
        elif noun.endswith("ies"):
            singular_noun = f"{noun[:-3]}y"
        elif "Entities" in noun:
            singular_noun = noun.replace("Entities", "Entity")
        elif noun.endswith("s"):
            singular_noun = noun[:-1]
    return singular_noun


def class_name_from_pointer(pointer: str) -> str:
    name: str = pointer
    if pointer.endswith("#/items/0"):
        name = class_name(depluralize(pointer[:-9]))
    elif pointer.endswith("#/items"):
        name = pluralize(pointer[:-7])
    elif pointer.endswith("#/0"):
        name = class_name(depluralize(pointer[:-3]))
    elif pointer == "pools#":
        name = pointer[:-1]
    elif pointer == "latest-runs#":
        name = "{}/response".format(pointer.rstrip("#"))
    name = _class_name_from_pointer(name)
    return name


class_name_from_pointer.__doc__ = getdoc(_class_name_from_pointer)


class Contractor:
    def __init__(self) -> None:
        self.client: Client = Client(
            (
                "https://proxy.us-west-2.map.my.com/sustainability-dev/"
                "api/experimental"
            ),
            oauth2_client_id="sustainability.etl",
            oauth2_client_secret_cerberus_path=(
                "app/sustainability/etl/client-secret"
            ),
            oauth2_token_url="https://api.aegis.mycloud.com/v1/prod/token",
            echo=True,
        )

    @property  # type: ignore
    @thesaurus_lru_cache(1, True)
    def thesaurus(self) -> Thesaurus:
        thesaurus: Thesaurus = Thesaurus(
            {  # type: ignore
                "latest-runs": {
                    self.client.request("/latest_runs", method="GET")
                },
                "pools": {self.client.request("/pools", method="GET")},
                "test": {self.client.request("/test", method="GET")},
                "dag-runs": set(),
                "post-dag-run-response": set(),
                "dag-paused": set(),
            }
        )
        latest_runs_response: Dict[str, List[Dict[str, Any]]]
        for latest_runs_response in thesaurus["latest-runs"]:  # type: ignore
            for latest_run in latest_runs_response["items"]:
                dag_id: str = latest_run["dag_id"]
                try:
                    thesaurus["dag-runs"].add(
                        self.client.request(
                            f"/dags/{dag_id}/dag_runs", method="GET"
                        )
                    )
                    thesaurus["post-dag-run-response"].add(
                        self.client.request(
                            f"/dags/{dag_id}/dag_runs",
                            method="POST",
                            form_data={"conf": ""},
                        )
                    )
                    thesaurus["dag-paused"].add(
                        self.client.request(
                            f"/dags/{dag_id}/paused", method="GET"
                        )
                    )
                    synonyms: Synonyms
                    is_paused: Optional[bool] = None
                    for synonyms in thesaurus["dag-paused"]:  # type: ignore
                        try:
                            is_paused = synonyms["is_paused"]  # type: ignore
                            break
                        except KeyError:
                            pass
                    if is_paused is None:
                        raise KeyError("is_paused")
                    thesaurus["dag-paused"].add(
                        self.client.request(
                            f"/dags/{dag_id}/paused/{str(is_paused).lower()}",
                            method="GET",
                        )
                    )
                except HTTPError as error:
                    # Sometimes deleted DAGs will be present in the list
                    # last DAG runs
                    if error.code in (400, 404):
                        continue
                    raise
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
