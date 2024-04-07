from pathlib import Path

import oapi
import sob
from oapi.model import Module
from oapi.oas import model

_PROJECT_PATH: Path = Path(__file__).absolute().parent.parent
OPENAPI_JSON: str = str(_PROJECT_PATH.joinpath("openapi.json"))
MODEL_PY: str = str(
    _PROJECT_PATH.joinpath("enablon_ingress_client", "model.py")
)


def get_openapi() -> model.OpenAPI:
    with open(OPENAPI_JSON, "r") as schema_io:
        assert isinstance(schema_io, sob.abc.Readable)
        open_api = oapi.model.OpenAPI(schema_io)
    return open_api


def main() -> None:
    openapi: model.OpenAPI = get_openapi()
    Module(openapi).save(MODEL_PY)


if __name__ == "__main__":
    main()
