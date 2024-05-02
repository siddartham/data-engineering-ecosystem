import json
import os
from collections import deque
from typing import IO, Dict, List
from warnings import warn

import oapi
import sob  # type: ignore
import yaml  # type: ignore
from daves_dev_tools.clean import delete_empty_directories
from daves_dev_tools.git.download import download
from sob.abc import JSONTypes
from sob.model import serialize

CERBERUS_URL: str = "https://prod.cerberus.mycloud.com"
PROJECT_PATH: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AIRFLOW_GIT_URL: str = "https://github.com/apache/airflow.git"
V1_OPENAPI_URL: str = (
    "https://gateway.us-west-2.map.my.com/airflow-client-test/"
    "api/v1/openapi.json"
)
GIT_V1_OPENAPI_PATH: str = "airflow/api_connexion/openapi/v1.yaml"
OPENAPI_SOURCE_DIRECTORY: str = os.path.join(PROJECT_PATH, "openapi", "source")
OPENAPI_FIXED_DIRECTORY: str = os.path.join(PROJECT_PATH, "openapi", "fixed")
V1_OPENAPI_FIXED_PATH: str = os.path.join(OPENAPI_FIXED_DIRECTORY, "v1.json")
MODEL_PATH: str = os.path.join(
    PROJECT_PATH, "map_airflow_client", "v1", "model.py"
)
CLIENT_PATH: str = os.path.join(
    PROJECT_PATH, "map_airflow_client", "v1", "client.py"
)


def get_open_api(schema_path: str) -> oapi.oas.model.OpenAPI:
    schema_io: IO[str]
    schema: Dict[str, JSONTypes]
    with open(schema_path, "r") as schema_io:
        if schema_path.endswith(".yaml") or schema_path.endswith(".yml"):
            schema = yaml.safe_load(schema_io)
        else:
            schema = json.load(schema_io)
    return oapi.oas.model.OpenAPI(schema)


def fix_open_api(
    open_api: oapi.oas.model.OpenAPI,
) -> None:
    pass


def download_from_git() -> str:
    """
    This can be used to generate the model prior to generating a client
    (whereas `download_from_map` requires the client to have been
    generated already).
    """
    files: List[str] = download(
        AIRFLOW_GIT_URL,
        files=(GIT_V1_OPENAPI_PATH,),
        directory=OPENAPI_SOURCE_DIRECTORY,
    )
    assert (
        files
    ), f'Could not download "{GIT_V1_OPENAPI_PATH}" from {AIRFLOW_GIT_URL}'
    path: str = os.path.join(
        OPENAPI_SOURCE_DIRECTORY, os.path.basename(GIT_V1_OPENAPI_PATH)
    )
    os.rename(files[0], path)
    delete_empty_directories(OPENAPI_SOURCE_DIRECTORY)
    deque(map(print, files), maxlen=0)
    return path


def download_from_map() -> str:
    from map_airflow_client.v1.client import Client

    client: Client = Client(
        "https://proxy.us-west-2.map.my.com/airflow-client-test/api/v1",
        oauth2_client_id="sustainability.etl",
        oauth2_client_secret_cerberus_path=(
            "app/sustainability/etl/client-secret"
        ),
        oauth2_token_url="https://api.aegis.mycloud.com/v1/prod/token",
        echo=False,
    )
    path: str = os.path.join(OPENAPI_SOURCE_DIRECTORY, "v1_map.json")
    with client.request(V1_OPENAPI_URL, method="GET") as url_io:
        with open(path, "w") as path_io:
            path_io.write(
                json.dumps(
                    json.loads(str(url_io.read(), encoding="utf-8")), indent=4
                )
            )
    return path


def update_model() -> oapi.oas.model.OpenAPI:
    os.makedirs(OPENAPI_SOURCE_DIRECTORY, exist_ok=True)
    os.makedirs(OPENAPI_FIXED_DIRECTORY, exist_ok=True)
    # Download from *MAP* the published Open API document (for reference only).
    try:
        download_from_map()
    except Exception:
        warn(sob.errors.get_exception_text())
    # Download the *latest* Open API document from Github
    # We use *this* document rather than the one from MAP because this way the
    # client will not break the next time someone updates the version of
    # Airflow used in their MAP cluster (and *newer* minor version are
    # backwards compatible).
    path: str = download_from_git()
    open_api = get_open_api(path)
    fix_open_api(open_api)
    fixed_io: IO[str]
    with open(
        os.path.join(
            OPENAPI_FIXED_DIRECTORY,
            os.path.basename(path).replace(".yaml", ".json"),
        ),
        "w",
    ) as fixed_io:
        fixed_io.write(serialize(open_api, indent=4))
    model_module: oapi.model.Module = oapi.model.Module(open_api)
    model_module.save(MODEL_PATH)
    return open_api


def update_client() -> None:
    open_api: oapi.oas.model.OpenAPI = get_open_api(V1_OPENAPI_FIXED_PATH)
    client_module: oapi.client.Module = oapi.client.Module(
        open_api,
        model_path=MODEL_PATH,
        imports=(
            (
                "from cerberus_assistant.decorate "
                "import apply_cerberus_path_arguments"
            ),
            ("from cerberus_assistant.config import CERBERUS_URL"),
        ),
        init_decorator=(
            "@apply_cerberus_path_arguments(\n"
            '    cerberus_url_parameter_name="cerberus_url",\n'
            '    oauth2_client_secret="oauth2_client_secret_cerberus_path",\n'
            ")"
        ),
        include_init_parameters=(
            "url",
            "oauth2_client_id",
            "oauth2_client_secret",
            "oauth2_token_url",
            "timeout",
            "retry_number_of_attempts",
            "retry_for_errors",
            "retry_hook",
            "logger",
            "echo",
        ),
        add_init_parameters=(
            "cerberus_url: str = CERBERUS_URL",
            'oauth2_client_secret_cerberus_path: str = ""',
        ),
        add_init_parameter_docs=(
            (
                "cerberus_url (str): The root URL for the Cerberus API where\n"
                "your secrets are stored."
            ),
            (
                'oauth2_client_secret_cerberus_path (str) = "": A Cerberus '
                "secure data path (including /key) wherein a username with "
                "which to authenticate can be found."
            ),
        ),
        init_parameter_defaults={
            "oauth2_token_url": (
                "https://api.aegis.mycloud.com/v1/prod/token"
            ),
            "retry_number_of_attempts": 3,
        },
    )
    client_module.save(CLIENT_PATH)


def main() -> None:
    update_model()
    update_client()


if __name__ == "__main__":
    main()
