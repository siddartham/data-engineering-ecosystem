from alembic import context  # type: ignore
from analytics_orm.alembic import migrations
from sqlalchemy.engine import URL, make_url  # type: ignore

from my_api_model.base import Base
from my_api_model.dialects import postgresql


def get_bind() -> URL:
    """
    Get the bind URL for this session
    """
    sqlalchemy_url: str = context.config.get_main_option(
        "sqlalchemy.url", default=""
    )
    assert sqlalchemy_url
    url: URL = make_url(sqlalchemy_url)
    assert isinstance(url, URL)
    if (url.username and url.password) or url.drivername == "sqlite":
        return url
    elif url.drivername == "postgresql" and url.database:
        database_name: str = url.database.lower()
        if database_name.endswith("_dev"):
            return postgresql.get_environment_connection_string("dev")
        elif database_name.endswith("_qa"):
            return postgresql.get_environment_connection_string("qa")
        elif database_name.endswith("_prod"):
            return postgresql.get_environment_connection_string("prod")
        else:
            raise ValueError(str(url))
    else:
        raise ValueError(str(url))


def main() -> None:
    bind: URL = get_bind()
    print(bind)
    migrations.run(metadata=Base.metadata, bind=bind, echo=True)


main()
