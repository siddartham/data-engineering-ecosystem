import enum
import functools
import os
import re
from collections import namedtuple
from datetime import date, datetime
from enum import Enum, auto
from functools import wraps
from logging import Logger, getLogger
from shlex import quote
from subprocess import CalledProcessError, check_output
from time import sleep
from types import ModuleType
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)
from unicodedata import normalize
from warnings import warn

from .errors import append_exception_text, get_exception_text

__all__: List[str] = [
    "lru_cache",
    "url_is_local",
    "get_qualified_name",
    "Undefined",
    "UNDEFINED",
    "run",
    "SUCCESS_FILE_NAME",
    "SUCCESS",
    "get_path_datetime_and_index",
    "is_date_partition_directory",
    "get_date_directory_name",
    "parse_datetime_string",
    "FileSortKey",
    "camel",
    "retry",
]


lru_cache: Callable[..., Any] = functools.lru_cache
log: Logger = getLogger(".".join(__name__.split(".")[:-1]))

SUCCESS_FILE_NAME: str = "_SUCCESS"
SUCCESS: bytes = bytes(())
_DIGITS: str = "0123456789"
_LOWERCASE_ALPHABET: str = "abcdefghijklmnopqrstuvwxyz"
_UPPERCASE_ALPHABET: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_ALPHANUMERIC_CHARACTERS = (
    f"{_DIGITS}" f"{_UPPERCASE_ALPHABET}" f"{_LOWERCASE_ALPHABET}"
)


def camel(string: str, capitalize: bool = False) -> str:
    """
    This function returns a camelCased representation of the input string.

    Parameters:

    - string (str): The string to be camelCased.

    - capitalize (bool):

      If this is `true`, the first letter will be capitalized.

    >>> print(camel('the birds and the bees'))
    theBirdsAndTheBees

    >>> print(camel('the birds and the bees', capitalize=True))
    TheBirdsAndTheBees

    >>> print(camel('the-birds-and-the-bees'))
    theBirdsAndTheBees

    >>> print(camel('**the - birds - and - the - bees**'))
    theBirdsAndTheBees

    >>> print(camel('FYI is an acronym'))
    FYIIsAnAcronym

    >>> print(camel('in-you-go'))
    inYouGo

    >>> print(camel('False'))
    false

    >>> print(camel('True'))
    true

    >>> print(camel('in'))
    in

    >>> print(camel('AB CD Efg', capitalize=True))
    ABCdEfg

    >>> print(camel('ABC DEF GHI', capitalize=True))
    AbcDefGhi

    >>> print(camel('ABC_DEF_GHI', capitalize=True))
    AbcDefGhi

    >>> print(camel('ABC DEF GHI'))
    abcDefGhi

    >>> print(camel('ABC_DEF_GHI'))
    abcDefGhi
    """
    index: int
    character: str
    string = normalize("NFKD", string)
    characters: List[str] = []
    all_uppercase: bool = string.upper() == string
    capitalize_next: bool = capitalize
    uncapitalize_next: bool = (not capitalize) and (
        len(string) < 2
        or all_uppercase
        or not (
            string[0] in _UPPERCASE_ALPHABET
            and string[1] in _UPPERCASE_ALPHABET
        )
    )
    for index, character in enumerate(string):
        if character in _ALPHANUMERIC_CHARACTERS:
            if capitalize_next:
                if all_uppercase:
                    uncapitalize_next = True
                elif capitalize or characters:
                    character = character.upper()
                    # This prevents two acronyms which are adjacent from
                    # retaining capitalization (since word separations would
                    # not be possible to identify if caps were kept for both)
                    if characters and (characters[-1] in _UPPERCASE_ALPHABET):
                        uncapitalize_next = True
            elif uncapitalize_next:
                if character in _LOWERCASE_ALPHABET:
                    uncapitalize_next = False
                else:
                    character = character.lower()
            characters.append(character)
            capitalize_next = False
        else:
            capitalize_next = True
            uncapitalize_next = False
    character_string = "".join(characters)
    return character_string


class _CharacterType(enum.Enum):
    DIGIT = enum.auto()
    LOWERCASE = enum.auto()
    UPPERCASE = enum.auto()
    OTHER = enum.auto()


def camel_split(string: str) -> Tuple[str, ...]:
    """
    Split a string of camelCased words into a tuple.

    Examples:

    >>> print(
    ...     '(%s)' % ', '.join(
    ...         "'%s'" % s for s in camel_split('theBirdsAndTheBees')
    ...     )
    ... )
    ('the', 'Birds', 'And', 'The', 'Bees')
    >>> print(
    ...     '(%s)' % ', '.join(
    ...         "'%s'" % s for s in camel_split('theBirdsAndTheBees123')
    ...     )
    ... )
    ('the', 'Birds', 'And', 'The', 'Bees', '123')
    >>> print(
    ...     '(%s)' % ', '.join(
    ...         "'%s'" % s for s in camel_split('theBirdsAndTheBeesABC123')
    ...     )
    ... )
    ('the', 'Birds', 'And', 'The', 'Bees', 'ABC', '123')
    >>> print(
    ...     '(%s)' % ', '.join(
    ...         "'%s'" % s for s in camel_split(
    ...             'the-Birds-&-The-Bs-ABC--123'
    ...         )
    ...     )
    ... )
    ('the', '-', 'Birds', '-&-', 'The', '-', 'Bs', '-', 'ABC', '--', '123')
    >>> print(
    ...     '(%s)' % ', '.join(
    ...         "'%s'" % s for s in camel_split('THEBirdsAndTheBees')
    ...     )
    ... )
    ('THE', 'Birds', 'And', 'The', 'Bees')
    """
    words: List[List[str]] = []
    preceding_character_type: Optional[_CharacterType] = None
    for character in string:
        character_type: _CharacterType = (
            _CharacterType.LOWERCASE
            if character in _LOWERCASE_ALPHABET
            else _CharacterType.DIGIT
            if character in _DIGITS
            else _CharacterType.UPPERCASE
            if character in _UPPERCASE_ALPHABET
            else _CharacterType.OTHER
        )
        if character_type == _CharacterType.LOWERCASE:
            if preceding_character_type == _CharacterType.LOWERCASE:
                # If following another lowercase character, a lowercase
                # character always continues that word
                words[-1].append(character)
            elif preceding_character_type == _CharacterType.UPPERCASE:
                if len(words[-1]) > 1:
                    # When following a multi-character uppercase word,
                    # the preceding word's last character should be removed
                    # and a new word created from that preceding character
                    # as well as the current lowercase character (until
                    # followed by a lowercase character, the preceding
                    # uppercase character was inferred to be part of an,
                    # however now we know it was either following an acronym,
                    # or following a single-character word)
                    words.append([words[-1].pop()] + [character])
                else:
                    # When following an uppercase character, a lowercase
                    # character should be added to the preceding word if that
                    # word has only one character thus far
                    words[-1].append(character)
            else:
                words.append([character])
            preceding_character_type = _CharacterType.LOWERCASE
        else:
            # Any type of character besides one from the *lowercase alphabet*
            # should start a new word if it follows a character of a
            # different type
            if preceding_character_type == character_type:
                words[-1].append(character)
            else:
                words.append([character])
            preceding_character_type = character_type
    return tuple("".join(word) for word in words)


@lru_cache()
def url_is_local(url: str) -> bool:
    localstack_hostname: str = os.environ.get(
        "LOCALSTACK_HOSTNAME", "localhost"
    )
    return bool(
        url.startswith(f"http://{localstack_hostname}")
        or url.startswith("http://127.0.0.1")
        or url.startswith("http://0.0.0.0")
    )


def get_qualified_name(
    type_or_module: Union[type, Callable, ModuleType]
) -> str:
    """
    >>> print(get_qualified_name(get_qualified_name))
    file_system_client.utilities.get_qualified_name

    >>> from file_system_client.base import FileSystem
    >>> print(get_qualified_name(FileSystem))
    file_system_client.base.FileSystem
    """
    assert callable(type_or_module) or isinstance(
        type_or_module, (type, ModuleType)
    ), (
        f"`{type_or_module}` is not an instance of "
        f"`type`, `collections.abc.Callable`, or `types.ModuleType`"
    )
    type_name: str
    # noinspection SpellCheckingInspection
    if isinstance(type_or_module, ModuleType):
        type_name = type_or_module.__name__
    else:
        type_name = ".".join(
            name_part
            for name_part in getattr(
                type_or_module,
                "__qualname__",
                getattr(type_or_module, "__name__"),
            ).split(".")
            if name_part[0] != "<"
        )
        if type_or_module.__module__ not in (
            "builtins",
            "__builtin__",
            "__main__",
            "__init__",
        ):
            type_name = type_or_module.__module__ + "." + type_name
    return type_name


_module_locals: Dict[str, Any] = locals()


class Undefined:
    """
    This class is intended to indicate that a parameter has not been passed
    to a keyword argument in situations where `None` is to be used as a
    meaningful value.
    """

    def __init__(self) -> None:
        """
        Only one instance of `Undefined` is permitted, so initialization
        checks to make sure this is the first use.
        """
        if "UNDEFINED" in _module_locals:
            raise RuntimeError(
                "%s may only be instantiated once." % repr(self)
            )

    def __repr__(self) -> str:
        """
        Represent instances of this class using the qualified name for the
        constant `UNDEFINED`.
        """
        representation = "UNDEFINED"
        if self.__module__ not in (
            "__main__",
            "builtins",
            "__builtin__",
            __name__,
        ):
            representation = "".join(
                [type(self).__module__, ".", representation]
            )
        return representation

    def __bool__(self) -> bool:
        """
        `UNDEFINED` cast as a boolean is `False` (as with `None`)
        """
        return False

    def __hash__(self) -> int:
        return 0

    def __eq__(self, other: Any) -> bool:
        """
        Another object is only equal to this if it shares the same id, since
        there should only be one instance of this class defined
        """
        return other is self


UNDEFINED: Undefined = Undefined()


def run(
    command: Sequence[str],
    echo: bool = True,
    env: Union[Dict[str, str], Sequence[Tuple[str, str]]] = (),
    **kwargs: Any,
) -> str:
    """
    This function runs a shell command, raises an error if a non-zero
    exit code is returned, and echo's both the command and output *if*
    the `echo` parameter is `True`.

    Parameters:

    - command (str|[str]): A shell command
    - echo (bool) = True: If `True`, the command and the output from the
      command will be printed to stdout
    - env ({str: str}|None) = None
    - **kwargs (typing.Any): Additional keyword arguments to pass to
      `subprocess.run`

    """
    if echo:
        command_str: str
        if isinstance(command, str):
            command_str = command
        else:
            command_str = " ".join(map(quote, command))
        print(command_str)
    kwargs.pop("shell", None)
    if env:
        kwargs.update(env=dict(env))
    try:
        output: str = check_output(
            command,
            encoding=kwargs.pop("encoding", "utf-8"),
            universal_newlines=kwargs.pop("universal_newlines", True),
            shell=isinstance(command, str),
            **kwargs,
        ).strip()
    except CalledProcessError as error:
        print(error.output)
        raise
    if echo:
        print(output)
    return output


PathDatetimeAndIndex = namedtuple(
    "PathDatetimeAndIndex", ("datetime", "index")
)


class FileSortKey(Enum):
    """
    This class defines types of file sorting behavior
    """

    DEFAULT = auto()
    MODIFIED = auto()
    NAME = auto()


def get_path_datetime_and_index(path: str) -> PathDatetimeAndIndex:
    """
    This function looks for, and returns, the top-most parent directory
    which appears to be a date-partition. For example:

    >>> get_path_datetime_and_index("prod/raw/date=2021-07-23-13-05").datetime
    datetime.datetime(2021, 7, 23, 13, 5)
    >>> get_path_datetime_and_index("prod/raw/date=2021-07-23-13-05").index
    2
    >>> get_path_datetime_and_index(
    ...     "prod/raw/date=2021-07-23-13-05/0001.json"
    # ... ).index
    2

    Parameters:

    - path (str)

    Returns: A tuple wherein the first item is a `datetime.datetime` instance,
    and the second item is an integer indicating the index at which the
    partition directory/sub-directory is nested.
    """
    if "=" not in path:
        raise ValueError(path)
    timestamp: Optional[datetime] = None
    timestamp_index: Optional[int] = None
    path_segment: str
    for index, path_segment in enumerate(path.rstrip("/ ").split("/")):
        if "=" in path_segment:
            parameter_name: str
            value: str
            parameter_name, value = path_segment.split("=")[:2]
            parameter_name = parameter_name.strip().lower()
            if ("date" in parameter_name) or ("time" in parameter_name):
                try:
                    timestamp = parse_datetime_string(value)
                except Exception as error:  # noqa
                    append_exception_text(
                        error, f"\nCould not find a timestamp in {repr(path)}"
                    )
                    raise error
                timestamp_index = index
    if not timestamp:
        raise ValueError(path)
    return PathDatetimeAndIndex(timestamp, timestamp_index)


def is_date_partition_directory(path: str) -> bool:
    try:
        path_datetime_and_index: PathDatetimeAndIndex = (
            get_path_datetime_and_index(path)
        )
        return path_datetime_and_index.index == (
            len(path.rstrip("/ ").split("/")) - 1
        )
    except ValueError:
        return False


def parse_datetime_string(datetime_string: str) -> datetime:
    try:
        return datetime(
            *map(  # type: ignore
                int, filter(None, re.split(r"[^\d]", datetime_string.strip()))
            )
        )
    except Exception as error:  # noqa
        append_exception_text(
            error,
            f'\nCould not parse "{datetime_string}" as a `datetime.datetime`',
        )
        raise error


def get_date_directory_name(
    date_or_datetime: Union[datetime, date, None] = None,
    prefix: str = "date_partition=",
    precision: int = 5,
) -> str:
    """
    Return a sub-directory name derived from the specified `date_or_datetime`.

    Parameters:

    - date_or_datetime (datetime.datetime|datetime.date|None) = None:
      The date or date + time from which to derive the name. If none is
      provided, the current date + time is used.
    - prefix (str) = "date_partition=": A prefix with which to prepend the
      formatted date/datetime string.
    - precision (int) = 5: The number of datetime components to include.
      The default precision is 5, which includes year + month + day + hour +
      minute. A precision of 6 would also include seconds, and a precision of
      7 would include seconds + microseconds.
    """
    if date_or_datetime is None:
        date_or_datetime = datetime.now()
    # The precision should be at least 1, or we have nothing to work with
    if not precision:
        raise ValueError(precision)
    # Make sure the year is four characters long
    name_components: Tuple[str, ...] = (
        f"0000{str(date_or_datetime.year)}"[-4:],
    )
    # Append month and day, if included in the `precision`
    datetime_component: int
    for datetime_component in (date_or_datetime.month, date_or_datetime.day)[
        : precision - 1
    ]:
        name_components += (f"00{str(datetime_component)}"[-2:],)
    # Further precision can only be used if an instance of `datetime.datetime`
    # was provided
    if isinstance(date_or_datetime, datetime):
        # All further components except for microseconds need 2 digits
        for datetime_component in (
            date_or_datetime.hour,
            date_or_datetime.minute,
            date_or_datetime.second,
        )[: precision - 3]:
            name_components += (f"00{str(datetime_component)}"[-2:],)
        # Microseconds need 6 digits
        if precision >= 7:
            name_components += (
                f"000000{str(date_or_datetime.microsecond)}"[-6:],
            )
    return f"{prefix}{'-'.join(name_components)}"


def _default_retry_hook(error: Exception) -> bool:
    assert error
    return True


def retry(
    errors: Union[Tuple[Type[Exception], ...], Type[Exception]] = Exception,
    retry_hook: Callable[[Exception], bool] = _default_retry_hook,
    number_of_attempts: int = 1,
) -> Callable:
    """
    This function decorates another, and causes the decorated function
    to be re-attempted a specified number of times, with exponential
    backoff, until the decorated function is successful or the maximum
    number of attempts is reached (in which case an exception is raised).

    Parameters:

    - errors: A sub-class of `Exception`, or a tuple of one or more
      sub-classes of `Exception`. The default is `Exception`, causing
      *all* errors to trigger a retry.
    - retry_hook: A function accepting as it's only argument the handled
      exception, and returning a boolean value indicating whether or not to
      retry the function.
    - number_of_attempts (int) = 1: The maximum number of times to attempt
      execution of the function, *including* the first execution. Please
      note that, because the default for this parameter is 1, this decorator
      will do *nothing* if this argument is not provided.
    """

    def decorating_function(function: Callable) -> Callable:
        attempt_number: int = 1

        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal attempt_number
            nonlocal number_of_attempts
            if number_of_attempts - attempt_number:
                try:
                    return function(*args, **kwargs)
                except errors as error:
                    if not retry_hook(error):
                        raise
                    warning_message: str = (
                        f"Attempt # {str(attempt_number)}:\n"
                        f"{get_exception_text()}"
                    )
                    warn(warning_message)
                    log.warning(warning_message)
                    sleep(2**attempt_number)
                    attempt_number += 1
                    return wrapper(*args, **kwargs)
            return function(*args, **kwargs)

        return wrapper

    return decorating_function
