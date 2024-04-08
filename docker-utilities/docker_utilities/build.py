import argparse
import functools
from enum import Enum
from typing import (
    Dict,
    Iterable,
    List,
    Mapping,
    Sequence,
    Tuple,
    Union,
)
from cerberus_assistant.decorate import apply_cerberus_path_arguments
from .config import SERVER, DOCKER, MULTI_PLATFORM_BUILD_CONTEXT
from ._utilities import get_tuple_str, check_call, check_output
from .login import login
from .exists import exists


class Platform(Enum):
    LINUX_AMD64: str = "linux/amd64"
    LINUX_AMD64_V2: str = "linux/amd64/v2"
    LINUX_AMD64_V3: str = "linux/amd64/v3"
    LINUX_ARM64: str = "linux/arm64"
    LINUX_ARM64_V8: str = "linux/arm64/v8"
    LINUX_RISCV64: str = "linux/riscv64"
    LINUX_PPC64LE: str = "linux/ppc64le"
    LINUX_S390X: str = "linux/s390x"
    LINUX_386: str = "linux/386"
    LINUX_MIPS64LE: str = "linux/mips64le"
    LINUX_MIPS64: str = "linux/mips64"
    LINUX_ARM_V7: str = "linux/arm/v7"
    LINUX_ARM_V6: str = "linux/arm/v6"


def _append_build_arguments(
    command: Tuple[str, ...],
    build_arguments: Union[Dict[str, str], Sequence[str], None],
) -> Tuple[str, ...]:
    key: str
    value: str
    if build_arguments:
        if isinstance(build_arguments, Mapping):
            for key, value in sorted(build_arguments.items()):
                command += ("--build-arg", f"{key}={repr(value)}")
        else:
            for value in sorted(build_arguments):
                command += ("--build-arg", value)
    return command


def _build(
    tags: Sequence[str],
    directory: str,
    file: str,
    push: bool,
    build_arguments: Union[Dict[str, str], Sequence[str], None],
) -> None:
    if isinstance(tags, str):
        tags = (tags,)
    command: Tuple[str, ...] = (
        DOCKER,
        "build",
    )
    if file:
        command += ("-f", file)
    tag: str
    for tag in tags:
        command += ("-t", tag)
    command += (directory,)
    command = _append_build_arguments(command, build_arguments)
    check_call(command)
    if push:
        for tag in tags:
            check_call((DOCKER, "push", tag))


def _docker_context_exists(name: str) -> bool:
    try:
        check_call((DOCKER, "context", "inspect", name))
        return True
    except Exception:
        return False


@functools.lru_cache()
def _create_multi_platform_build_context(
    context_name: str = MULTI_PLATFORM_BUILD_CONTEXT,
) -> str:
    check_call(
        (
            DOCKER,
            "run",
            "--privileged",
            "--rm",
            "tonistiigi/binfmt",
            "--install",
            "all",
        )
    )
    if not _docker_context_exists(context_name):
        check_call(
            (
                DOCKER,
                "context",
                "create",
                context_name,
            )
        )
    container_name: str = check_output(
        (
            DOCKER,
            "buildx",
            "create",
            "--driver",
            "docker-container",
            context_name,
        )
    ).strip()
    check_call(
        (
            DOCKER,
            "context",
            "use",
            context_name,
        )
    )
    return container_name


def _buildx_build(
    tags: Sequence[str],
    directory: str,
    file: str,
    push: bool,
    load: bool,
    platforms: Tuple[str, ...],
    builder: str,
    no_cache: bool,
    build_arguments: Union[Dict[str, str], Sequence[str], None],
) -> None:
    if isinstance(tags, str):
        tags = (tags,)
    command: Tuple[str, ...] = (
        DOCKER,
        "buildx",
        "build",
        "--platform",
        ",".join(platforms),
    )
    if file:
        command += ("-f", file)
    uri: str
    for uri in tags:
        command += ("-t", uri)
    if push:
        command += ("--push",)
    if load:
        command += ("--load",)
    if no_cache:
        command += ("--no-cache",)
    if builder:
        command += (
            "--builder",
            builder,
        )
    command += (directory,)
    command = _append_build_arguments(command, build_arguments)
    check_call(command)


@apply_cerberus_path_arguments(
    user="user_cerberus_path",
    password="password_cerberus_path",
    server="server_cerberus_path",
)
def build(
    tags: Sequence[str],
    *,
    directory: str = ".",
    file: str = "",
    platforms: Iterable[Union[Platform, str]] = (),
    user: str = "",
    password: str = "",
    server: str = SERVER,
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    server_cerberus_path: str = "",
    push: bool = True,
    skip_existing: bool = False,
    build_arguments: Union[Dict[str, str], List[str], None] = None,
) -> bool:
    """
    Build, and (optionally) push, a docker image to a Managed Spark ECR
    repository.

    Parameters:

    - tags ([str])
    - file (str) = "Dockerfile: The file path/name of the Dockerfile to build
    - directory (str) = "."
    - platforms ([str|docker_utilities.build.Platform]) = ():
      If this argument is provided, a multi-platform
      build will be performed. If this argument is not provided,
      a single-platform build will be performed.
    - user (str) = "": A GID username with which to authenticate.
    - password (str) = "": A GID password with which to authenticate.
    - server (str) = "": A remote Docker registry URI.
    - user_cerberus_path (str) = "": A Cerberus secure data path (including /
      key) wherein a GID username with which to authenticate can be found.
    - password_cerberus_path (str) = "": A Cerberus secure data path (including
      /key) wherein a GID password with which to authenticate can be found.
    - server_cerberus_path (str) = "": A Cerberus secure data path (including
      /key) wherein the server URI (host|host:port) can be found.
    - skip_existing (bool) = False: If `False`, the function will raise an
      error if the artifact already exists, otherwise it will silently skip
      deploying the artifact
    - build_arguments ({str: str}|[str]|None) = None

    Returns `True` if images were built and deployed, or `False` if
    `skip_existing` and all images already existed.
    """
    assert tags
    if isinstance(tags, str):
        tags = (tags,)
    if user and password and server:
        login(user=user, password=password, server=server)
    platforms = get_tuple_str(platforms)
    assert all(map(str.__len__, platforms))
    if skip_existing and all(map(exists, tags)):
        return False
    if platforms:
        _buildx_build(
            tags,
            directory,
            file,
            push,
            False if push else True,
            platforms,
            _create_multi_platform_build_context(),
            False,
            build_arguments,
        )
    else:
        _build(tags, directory, file, push, build_arguments)
    return True


def main() -> None:
    """
    This function is the entry point for using this script as a CLI.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="docker-utilities build",
        description="Build and (optionally) push an image",
    )
    parser.add_argument(
        "--tag",
        "-t",
        action="append",
        type=str,
        default=[],
    )
    parser.add_argument(
        "--file",
        "-f",
        type=str,
        default="Dockerfile",
        help="The path to a Dockerfile",
    )
    parser.add_argument(
        "--directory",
        "-d",
        type=str,
        default=".",
        help="The build context directory (defaults to the current directory)",
    )
    parser.add_argument(
        "--platform",
        action="append",
        type=str,
        default=[],
        help=(
            "Which platform/architecture(s) to build for "
            '(for example: "linux/amd64" or "linux/arm64").'
        ),
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help=(
            "If `True`, skip this build if the image already "
            "exists on the remote server"
        ),
    )
    parser.add_argument(
        "--user",
        "-u",
        type=str,
        default="",
    )
    parser.add_argument(
        "--password",
        "-p",
        type=str,
        default="",
    )
    parser.add_argument(
        "--server",
        "-s",
        type=str,
        default="",
    )
    parser.add_argument(
        "--user-cerberus-path",
        "-ucp",
        type=str,
        default="",
    )
    parser.add_argument(
        "--password-cerberus-path",
        "-pcp",
        type=str,
        default="",
    )
    parser.add_argument(
        "--server-cerberus-path",
        "-scp",
        type=str,
        default="",
    )
    parser.add_argument(
        "--no-push",
        action="store_true",
        help="If `True`, don't push this build",
    )
    parser.add_argument(
        "--build-arg",
        "-ba",
        action="append",
        type=str,
        default=[],
    )
    namespace: argparse.Namespace = parser.parse_args()
    build(
        tags=namespace.tag,
        file=namespace.file,
        directory=namespace.directory,
        platforms=namespace.platform,
        push=not namespace.no_push,
        skip_existing=namespace.skip_existing,
        build_arguments=namespace.build_arg,
        **dict(
            filter(
                all,
                (
                    ("user", namespace.user),
                    ("password", namespace.password),
                    ("server", namespace.server),
                    ("user_cerberus_path", namespace.user_cerberus_path),
                    (
                        "password_cerberus_path",
                        namespace.password_cerberus_path,
                    ),
                    ("server_cerberus_path", namespace.server_cerberus_path),
                ),
            )
        ),
    )


if __name__ == "__main__":
    main()
