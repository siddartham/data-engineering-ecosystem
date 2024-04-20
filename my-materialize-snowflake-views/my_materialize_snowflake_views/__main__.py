import argparse
import logging
from typing import Optional, Tuple

from analytics_etl.concurrency import (
    Concurrency,
    add_parser_concurrency_argument,
    get_concurrency_from_arguments,
)

from .broker import Broker
from .config import DEFAULT_CONCURRENCY


def materialize(
    environment: str,
    echo: bool = False,
    parallelism: Optional[int] = None,
    concurrency: Concurrency = DEFAULT_CONCURRENCY,
    include: Tuple[str, ...] = (),
    exclude: Tuple[str, ...] = (),
) -> None:
    Broker(
        environment=environment,
        parallelism=parallelism,
        concurrency=concurrency,
        echo=echo,
    ).materialize(include=include, exclude=exclude)


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--parallelism", action="store", type=int, default=None
    )
    parser.add_argument(
        "-l",
        "--log",
        action="store",
        type=str,
        default=None,
        help="Log output path",
    )
    add_parser_concurrency_argument(parser, default=DEFAULT_CONCURRENCY)
    parser.add_argument(
        "-e",
        "--echo",
        action="store_const",
        const=True,
        default=False,
        help="Echo requests/responses",
    )
    parser.add_argument("environment", help="map-dev | map-qa | map-prod")
    parser.add_argument(
        "--include",
        type=str,
        action="append",
        default=[],
        help=(
            'One or more tables ("materialized views") to refresh. '
            'If this argument is not provided, all "materialized view" tables '
            "will be refreshed"
        ),
    )
    parser.add_argument(
        "--exclude",
        type=str,
        action="append",
        default=[],
        help=(
            'One or more tables ("materialized views") to exclude (not '
            'refresh). If this argument is not provided, all "materialized '
            'view" tables will be refreshed.'
        ),
    )
    arguments: argparse.Namespace = parser.parse_args()
    concurrency: Concurrency = get_concurrency_from_arguments(
        arguments, default=DEFAULT_CONCURRENCY
    )
    if arguments.log:
        logging.basicConfig(filename=arguments.log, level=logging.INFO)
    materialize(
        environment=arguments.environment,
        echo=arguments.echo,
        parallelism=arguments.parallelism,
        concurrency=concurrency,
        include=tuple(arguments.include),
        exclude=tuple(arguments.exclude),
    )


if __name__ == "__main__":
    main()
