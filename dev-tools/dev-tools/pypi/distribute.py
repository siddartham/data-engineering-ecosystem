import runpy
import sys

from ..config import BMX_USER, CERBERUS_URL, BMX_CERBERUS_PATH


def main() -> None:
    """
    A proxy for `daves-dev-tools distribute`.
    """
    sys.argv += [
        "--repository-url",
        "https://artifactory.company.com/artifactory/api/pypi/python-local",
        "-u",
        BMX_USER,
        "--cerberus-url",
        CERBERUS_URL,
        "--cerberus-path",
        BMX_CERBERUS_PATH,
    ]
    runpy.run_module("daves_dev_tools.distribute", run_name="__main__")
