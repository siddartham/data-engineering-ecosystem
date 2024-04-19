import sys
from dataclasses import dataclass
from subprocess import check_output, list2cmdline
from traceback import format_exception
from typing import Any, Iterable, Optional, Tuple
from warnings import warn

import pkg_resources
from packaging.version import Version, parse


@dataclass
class _Version:
    """
    Instances of this class can be be passed as `self` in a call
    to `packaging.version.Version.__str__`, and thereby can facilitate
    operations to mimic mutability for the aforementioned class.
    """

    epoch: int
    release: Tuple[int, ...]
    pre: Any
    post: Any
    dev: Any
    local: Any


def _get_sustainability_model_deviation_version_specifier(
    deviation: int,
) -> str:
    installed_version: Version = parse(
        pkg_resources.get_distribution("nike-sustainability-model").version
    )
    specificity: int = deviation + 1
    greater_or_equal_specificity: bool = specificity >= len(
        installed_version.release
    )
    version_specifier: _Version = _Version(
        epoch=installed_version.epoch,
        # Truncate the updated version requirement at the same
        # level of specificity as the old
        release=installed_version.release[:specificity],
        pre=(installed_version.pre if greater_or_equal_specificity else None),
        post=(
            installed_version.post if greater_or_equal_specificity else None
        ),
        dev=(installed_version.dev if greater_or_equal_specificity else None),
        local=(
            installed_version.local if greater_or_equal_specificity else None
        ),
    )
    return Version.__str__(version_specifier)  # type: ignore


def update_sustainability_model(
    deviation: int = 1,
    extras: Iterable[str] = (),
    dry_run: bool = False,
) -> Optional[Exception]:
    """
    Upgrade the installed version of `nike-sustainability-model`, and
    return `None` if successful (otherwise return the error).

    Parameters:

     - deviation (int) = 1: The number of version specifier parts with which to
      maintain fidelity. A deviation of `0` permits all upgrades (including
      major version upgrades). A deviation of `1` permits minor and patch
      version upgrades. A deviation of `0` permits only patch version
      upgrades.
     - extras ((str,)|str) = (): One or more package extras to include in the
      upgrade.
     - dry_run (bool) = False: If `True`, commands will be printed, but not
      executed (for debugging)
    """
    print("Attempting to upgrade nike-sustainability-model")
    version_specifier: str = ""
    operator: str = ""
    if deviation:
        version_specifier = (
            _get_sustainability_model_deviation_version_specifier(deviation)
        )
        if version_specifier:
            operator = "~="
    extras_str: str = ""
    if extras:
        if isinstance(extras, str):
            extras_str = f"[{extras.strip('[] ')}]"
        else:
            extras_str = f"[{','.join(extras)}]"
    command: Tuple[str, ...] = (
        sys.executable,
        "-m",
        "pip",
        "install",
        "--upgrade",
        (
            f"nike-sustainability-model{extras_str}"
            f"{operator}{version_specifier}"
        ),
        "--extra-index-url",
        (
            "https://artifactory.nike.com/artifactory/api/pypi/python-local/"
            "simple"
        ),
    )
    print(list2cmdline(command))
    if not dry_run:
        try:
            check_output(
                command,
                encoding="utf-8",
                universal_newlines=True,
            ).strip()
        except Exception as error:
            warn(
                "Unable to upgrade nike-sustainability-model:\n"
                f'{"".join(format_exception(*sys.exc_info()))}'
            )
            return error
        pkg_resources.working_set.entries = []
        pkg_resources.working_set.__init__()  # type: ignore
        model_version: str = pkg_resources.get_distribution(
            "nike-sustainability-model"
        ).version
        print(f"nike-sustainability-model version: {model_version}")
    return None
