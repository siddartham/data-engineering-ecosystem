import unittest
from typing import Any, Callable

from analytics_orm.postgresql import (
    DEFAULT_DATABASE,
    DEFAULT_HOST,
    DEFAULT_PORT,
    DEFAULT_USER,
    get_connection_url,
)
from analytics_orm.utilities import (
    apply_conditional_defaults,
    apply_environment_defaults,
    is_current_user_human,
)


class TestBroker(unittest.TestCase):
    """
    TODO
    """

    def test_apply_conditional_defaults(self) -> None:
        """
        Test the functionality of the
        `@analytics_orm.utilities.apply_conditional_defaults()` decorator
        """

        def is_dev(
            function: Callable[..., Any],
            environment: str = "",
            *args: Any,
            **kwargs: Any,
        ) -> bool:
            return environment.lower() == "dev"

        def is_qa(
            function: Callable[..., Any],
            environment: str = "",
            *args: Any,
            **kwargs: Any,
        ) -> bool:
            return environment.lower() == "qa"

        def is_prod(
            function: Callable[..., Any],
            environment: str = "",
            *args: Any,
            **kwargs: Any,
        ) -> bool:
            return environment.lower() == "prod"

        @apply_conditional_defaults(
            is_dev,
            user="dev-user",
            password="dev-password",
            host="dev-host",
            database="dev",
        )
        @apply_conditional_defaults(
            is_qa,
            user="qa-user",
            password="qa-password",
            host="qa-host",
            database="qa",
        )
        @apply_conditional_defaults(
            is_prod,
            user="prod-user",
            password="prod-password",
            host="prod-host",
            database="prod",
        )
        def get_environment_connection_string(
            environment: str,
            user: str = DEFAULT_USER,
            password: str = "",
            host: str = DEFAULT_HOST,
            port: int = DEFAULT_PORT,
            database: str = DEFAULT_DATABASE,
        ) -> str:
            assert environment
            return str(
                get_connection_string(
                    user=user,
                    password=password,
                    host=host,
                    port=port,
                    database=database,
                )
            )

        assert get_environment_connection_string("dev") == (
            "postgresql://dev-user:dev-password@dev-host:5432/dev"
        )
        assert get_environment_connection_string("qa") == (
            "postgresql://qa-user:qa-password@qa-host:5432/qa"
        )
        assert get_environment_connection_string("prod") == (
            "postgresql://prod-user:prod-password@prod-host:5432/prod"
        )
        assert get_environment_connection_string("dev", user=None) == (
            "postgresql://dev-user:dev-password@dev-host:5432/dev"
        )
        assert get_environment_connection_string("qa", user=None) == (
            "postgresql://qa-user:qa-password@qa-host:5432/qa"
        )
        assert get_environment_connection_string("prod", user=None) == (
            "postgresql://prod-user:prod-password@prod-host:5432/prod"
        )
        assert (
            get_environment_connection_string("dev", user="explicit-user")
            == "postgresql://explicit-user:dev-password@dev-host:5432/dev"
        )
        assert (
            get_environment_connection_string("qa", user="explicit-user")
            == "postgresql://explicit-user:qa-password@qa-host:5432/qa"
        )
        assert get_environment_connection_string(
            "prod", user="explicit-user"
        ) == ("postgresql://explicit-user:prod-password@prod-host:5432/prod")

    def test_apply_environment_defaults(self) -> None:
        """
        Test the functionality of the
        `@analytics_orm.utilities.apply_environment_defaults()` decorator
        """

        @apply_environment_defaults(
            "dev",
            user="dev-user",
            password="dev-password",
            host="dev-host",
            database="dev",
        )
        @apply_environment_defaults(
            "qa",
            user="qa-user",
            password="qa-password",
            host="qa-host",
            database="qa",
            not_included_argument="?",
        )
        @apply_environment_defaults(
            "prod",
            user="prod-user",
            password="prod-password",
            host="prod-host",
            database="prod",
            not_included_argument="?",
        )
        def get_environment_connection_string(
            environment: str,
            user: str = DEFAULT_USER,
            password: str = "",
            host: str = DEFAULT_HOST,
            port: int = DEFAULT_PORT,
            database: str = DEFAULT_DATABASE,
        ) -> str:
            assert environment
            return str(
                get_connection_string(
                    user=user,
                    password=password,
                    host=host,
                    port=port,
                    database=database,
                )
            )

        assert get_environment_connection_string("dev") == (
            "postgresql://dev-user:dev-password@dev-host:5432/dev"
        )
        assert get_environment_connection_string("qa") == (
            "postgresql://qa-user:qa-password@qa-host:5432/qa"
        )
        assert get_environment_connection_string("prod") == (
            "postgresql://prod-user:prod-password@prod-host:5432/prod"
        )
        assert get_environment_connection_string("dev", user=None) == (
            "postgresql://dev-user:dev-password@dev-host:5432/dev"
        )
        assert get_environment_connection_string("qa", user=None) == (
            "postgresql://qa-user:qa-password@qa-host:5432/qa"
        )
        assert get_environment_connection_string("prod", user=None) == (
            "postgresql://prod-user:prod-password@prod-host:5432/prod"
        )
        assert (
            get_environment_connection_string("dev", user="explicit-user")
            == "postgresql://explicit-user:dev-password@dev-host:5432/dev"
        )
        assert (
            get_environment_connection_string("qa", user="explicit-user")
            == "postgresql://explicit-user:qa-password@qa-host:5432/qa"
        )
        assert get_environment_connection_string(
            "prod", user="explicit-user"
        ) == ("postgresql://explicit-user:prod-password@prod-host:5432/prod")

    def test_is_current_user_human(self) -> None:
        # We don't care what the result is, so long as getting it doesn't
        # produce an error
        is_current_user_human()


if __name__ == "__main__":
    unittest.main()
