"""
This script retrieves all tests from
https://github.com/siddartham/my-datastore-etl-wrapper, and
uses these tests to validate this package's functionality
"""

from daves_dev_tools.git.download import download
from cerberus_assistant.get import get_secret

GITHUB_USER: str = "a-github-actions-user"
GITHUB_PASSWORD_CERBERUS_PATH: str = f"app/team/github/{GITHUB_USER}"


def main() -> None:
    download(
        (
            "https://github.com/siddartham"
            "/my-datastore-etl-wrapper.git"
        ),
        files=("tests/*.yml", "tests/*.py"),
        user=GITHUB_USER,
        password=get_secret(GITHUB_PASSWORD_CERBERUS_PATH),
    )


if __name__ == "__main__":
    main()
