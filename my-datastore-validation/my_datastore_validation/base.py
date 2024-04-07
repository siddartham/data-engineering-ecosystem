from abc import abstractmethod
from itertools import chain, starmap
from multiprocessing.pool import Pool
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Iterable,
    Sequence,
    Tuple,
    Type,
    Union,
)

from orm_framework import validation
from orm_framework.errors import ValidationError
from orm_framework.utilities import iter_recursive_subclasses
from my_datastore_etl_wrapper.utilities import alert
from my_datastore_orm.base import Base
from sqlalchemy.engine.base import Connection  # type: ignore
from sqlalchemy.engine.base import Engine  # type: ignore
from sqlalchemy.engine.create import create_engine  # type: ignore
from sqlalchemy.engine.url import URL, make_url  # type: ignore
from sqlalchemy.sql.schema import ForeignKeyConstraint, Table  # type: ignore

get_snowflake_bind_environment: Callable[..., str]
try:
    from my_datastore_orm.dialects.snowflake import (
        get_bind_environment as get_snowflake_bind_environment,
    )
except ImportError:

    def get_snowflake_bind_environment(bind: Any) -> str:
        return ""


get_hive_bind_environment: Callable[..., str]
try:
    from my_datastore_orm.dialects.hive import (  # type: ignore  # noqa
        get_bind_environment as get_hive_bind_environment,
    )
except ImportError:

    def get_hive_bind_environment(bind: Any) -> str:
        return ""


cerberus_path: str = "app/sustainability/bmx/a.BMX.SUSTAINABILITY"


class BaseValidation:
    """
    This class invoke a declarative base
    against a `bind`  to perform introspection-inferred .
    """

    def __init__(
        self,
        base: Type[Base],
        bind: Union[Engine, Connection, URL, str, None] = None,
        ignore_foreign_keys: Union[
            Sequence[str], Callable[[ForeignKeyConstraint], bool], None
        ] = None,
        exclude_from_cache_validation: Union[
            Sequence[str], Callable[[Table], bool], None
        ] = None,
        only: Sequence[str] = (),
        echo: bool = False,
    ) -> None:
        if bind is None:
            bind = base.metadata.bind
            if isinstance(bind, Engine):
                bind.echo = echo
                bind = bind.connect()
        else:
            if isinstance(bind, str):
                bind = make_url(bind)
            if isinstance(bind, URL):
                bind = create_engine(bind, echo=echo)
            if isinstance(bind, Engine):
                bind.echo = echo
                bind = bind.connect()
            base.metadata.bind = bind
        if TYPE_CHECKING:
            assert isinstance(bind, Connection)
        assert (
            bind
        ), "A bind is required in order to validate a declarative base"
        self.base: Type[Base] = base
        self.bind: Connection = bind
        self.ignore_foreign_keys: Union[
            Sequence[str], Callable[[ForeignKeyConstraint], bool], None
        ] = ignore_foreign_keys
        self.exclude_from_cache_validation: Union[
            Sequence[str], Callable[[Table], bool], None
        ] = exclude_from_cache_validation
        self.only: Sequence[str] = only
        self.echo: bool = echo

    def __reduce__(self) -> Tuple[Callable[..., "BaseValidation"], Tuple]:
        url: str
        if isinstance(self.bind, Engine):
            url = str(self.bind.url)
        elif isinstance(self.bind, Connection):
            url = str(self.bind.engine.url)
        else:
            url = str(url)
        return self.__class__, (
            self.base,
            url,
            self.ignore_foreign_keys,
            self.exclude_from_cache_validation,
            self.only,
            self.echo,
        )

    @abstractmethod
    def validate(self) -> Iterable[ValidationError]:
        """
        implemented for explicit use to invoke
        orm_framework.validations.validate
        """
        yield from validation.validate(
            self.base,
            self.bind,
            ignore_foreign_keys=self.ignore_foreign_keys,
            exclude_from_cache_validation=(self.exclude_from_cache_validation),
            only=self.only,
            raise_exceptions=False,
        )

    def __call__(self) -> Iterable[Exception]:
        yield from self.validate()


def _validate_class(
    cls: Type[BaseValidation],
    base: Type[Base],
    bind: str,
    ignore_foreign_keys: Union[
        Sequence[str], Callable[[ForeignKeyConstraint], bool], None
    ],
    exclude_from_cache_validation: Union[
        Sequence[str], Callable[[Table], bool], None
    ],
    only: Sequence[str] = (),
    echo: bool = False,
    return_type: type = str,
) -> Union[Tuple[str, ...], Tuple[ValidationError, ...]]:
    print(f"Executing validation: {cls.__module__}.{cls.__name__}")
    errors: Iterable[ValidationError]
    if cls is BaseValidation:
        errors = cls(
            base,
            bind,
            ignore_foreign_keys=ignore_foreign_keys,
            exclude_from_cache_validation=(exclude_from_cache_validation),
            only=only,
            echo=echo,
        ).validate()
    else:
        errors = cls(base, bind, only=only, echo=echo).validate()
    return tuple(  # type: ignore
        map(repr, errors) if issubclass(return_type, str) else errors
    )


def validate(
    base: Type[Base],
    bind: Union[Engine, Connection, URL, str, None] = None,
    ignore_foreign_keys: Union[
        Sequence[str], Callable[[ForeignKeyConstraint], bool], None
    ] = None,
    exclude_from_cache_validation: Union[
        Sequence[str], Callable[[Table], bool], None
    ] = None,
    only: Sequence[str] = (),
    echo: bool = False,
    return_type: type = str,
) -> Union[Tuple[str, ...], Tuple[ValidationError, ...]]:
    """
    Parameters:

    - base (my_datastore_orm.base.Base)
    - bind (
        sqlalchemy.engine.base.Engine |
        sqlalchemy.engine.base.Connection |
        sqlalchemy.engine.url.URL |
        str
      )
    - ignore_foreign_keys ([str])
    - exclude_from_cache_validation ([str])
    - only ([str])
    - echo (bool)
    - return_type (type) = str:
      (str|Exception) If this is `str` (the
      default), an alert will be generated and sent, if errors are encountered.
      Otherwise, errors will only be returned.
    """
    assert return_type in (str, Exception)
    validation_classes: Tuple[Type[BaseValidation]] = (  # type: ignore
        BaseValidation,
    ) + tuple(iter_recursive_subclasses(BaseValidation))
    number_of_validations: int = len(validation_classes)
    if base.metadata.bind:
        if not bind:
            bind = base.metadata.bind
    # Get a connection string bind, so that the bind is pickleable
    if isinstance(bind, Connection):
        bind = bind.engine
    if isinstance(bind, Engine):
        bind = bind.url
    url: URL
    if isinstance(bind, URL):
        url = bind
        bind = str(bind)
    else:
        assert isinstance(bind, str)
        url = make_url(url)
    # External browser authentication breaks with multiprocessing, so
    # we have to use single-threading for local execution
    starmap_: Callable[[Callable, Iterable[Any]], Iterable[Any]]
    if url.query.get("authenticator", "") == "externalbrowser" or (
        return_type is not str
    ):
        starmap_ = starmap
    else:
        starmap_ = Pool(number_of_validations).starmap
    errors: Union[Tuple[ValidationError, ...], Tuple[str, ...]] = tuple(
        chain(
            *starmap_(
                _validate_class,
                zip(
                    validation_classes,
                    (base,) * number_of_validations,
                    (bind,) * number_of_validations,
                    (ignore_foreign_keys,) * number_of_validations,
                    (exclude_from_cache_validation,) * number_of_validations,
                    (only,) * number_of_validations,
                    (echo,) * number_of_validations,
                    (return_type,) * number_of_validations,
                ),
            ),
        )
    )
    if return_type is str:
        body: str = "\n\n".join(errors)  # type: ignore
        if body:
            alert(
                environment=(
                    get_snowflake_bind_environment(bind)
                    or get_hive_bind_environment(bind)
                    or "dev"
                ),
                subject="My DataStore Validation Errors",
                body=body,
            )
    return errors
