import subprocess
from enum import Enum
from typing import Iterable, Sequence, Tuple, Union


def _iter_censored_command(command: Sequence[str]) -> Iterable[str]:
    preceding_argument: str = ""
    argument: str
    for argument in command:
        if preceding_argument == "--password":
            yield "***"
        else:
            yield argument
        preceding_argument = argument


def check_call(command: Sequence[str], echo: bool = True) -> None:
    if echo:
        print()
        print(subprocess.list2cmdline(_iter_censored_command(command)))
    subprocess.check_call(command)


def check_output(command: Sequence[str], echo: bool = True) -> str:
    if echo:
        print()
        print(subprocess.list2cmdline(_iter_censored_command(command)))
        return subprocess.check_output(command, encoding="utf-8")
    return subprocess.check_output(
        command, encoding="utf-8", stderr=subprocess.STDOUT
    )


def get_tuple_str(
    value: Union[Iterable[Union[str, Enum]], Enum]
) -> Tuple[str, ...]:
    if isinstance(value, (str, Enum)):
        value = (value,)
    return tuple(map(_get_enum_str_value, value))


def _get_enum_str_value(enum_item: Union[Enum, str]) -> str:
    if isinstance(enum_item, Enum):
        assert isinstance(enum_item.value, str)
        return enum_item.value
    else:
        assert isinstance(enum_item, str)
        return enum_item
