import unittest

from cerberus_assistant.decorate import apply_cerberus_path_arguments
from cerberus_assistant.get import get_secret

SECRET_PATH: str = "app/sample-application/sample-secure-data-path/KEY"
AMAZON_RESOURCE_NAME: str = (
    "arn:aws:iam::1234567890:role/my-github-actions-runner"
)


@apply_cerberus_path_arguments(value="value_cerberus_path")
def return_value(
    value: str = "",
    value_cerberus_path: str = "",
    cerberus_arn: str = AMAZON_RESOURCE_NAME,
) -> str:
    return value


class TestDecorate(unittest.TestCase):
    """
    Unit tests for the `cerberus_assistant.get`  module.
    Unit tests for the `cerberus_assistant.get`  module.
    """

    def test_apply_cerberus_path_arguments(self) -> None:
        assert return_value(value=get_secret(SECRET_PATH)) == return_value(
            value_cerberus_path=SECRET_PATH
        )


if __name__ == "__main__":
    unittest.main()
