import sys
import unittest
from subprocess import check_call, check_output

from cerberus_assistant._utilities import split_secret_path
from cerberus_assistant.delete import delete_secrets
from cerberus_assistant.get import get_secret
from cerberus_assistant.put import put_secret, put_secrets

SECRETS_PATH: str = "app/cerberus-assistant-sandbox/test-secrets"
SECRETS_KEY: str = "test-secrets"
SECRETS_KEY_PATH: str = f"{SECRETS_PATH}/{SECRETS_KEY}"
SECRETS_VALUE: str = "test-secrets-value"
SECRET_KEY_PATH: str = "app/cerberus-assistant-sandbox/test-secret/test-secret"
SECRET_VALUE: str = "test-secret-value"


class TestGetPutDelete(unittest.TestCase):
    def test_secrets(self) -> None:
        put_secrets(SECRETS_PATH, {SECRETS_KEY: SECRETS_VALUE})
        assert get_secret(SECRETS_KEY_PATH) == SECRETS_VALUE
        delete_secrets(SECRETS_PATH)

    def test_secret(self) -> None:
        put_secret(SECRET_KEY_PATH, SECRET_VALUE)
        assert get_secret(SECRET_KEY_PATH) == SECRET_VALUE
        key: str
        path: str
        path, key = split_secret_path(SECRET_KEY_PATH)
        delete_secrets(path)

    def test_cli(self) -> None:
        check_call(
            (
                sys.executable,
                "-m",
                "cerberus_assistant",
                "put",
                SECRET_KEY_PATH,
                SECRET_VALUE,
            )
        )
        assert (
            SECRET_VALUE
            == check_output(
                (
                    sys.executable,
                    "-m",
                    "cerberus_assistant",
                    "get",
                    SECRET_KEY_PATH,
                ),
                encoding="utf-8",
                universal_newlines=True,
            ).rstrip()
        )
        key: str
        path: str
        path, key = split_secret_path(SECRET_KEY_PATH)
        check_call(
            (
                sys.executable,
                "-m",
                "cerberus_assistant",
                "delete",
                path,
            )
        )


if __name__ == "__main__":
    unittest.main()
