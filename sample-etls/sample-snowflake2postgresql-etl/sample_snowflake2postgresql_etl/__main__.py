import argparse
import logging
from my_datastore_etl.concurrency import (
    Concurrency,
    add_parser_concurrency_argument,
    get_concurrency_from_arguments,
)
from .broker import Broker


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
    add_parser_concurrency_argument(
        parser, default=Concurrency.MULTIPROCESSING
    )
    parser.add_argument(
        "-e",
        "--echo",
        action="store_true",
        help="Echo requests/responses",
    )
    parser.add_argument(
        "-lo",
        "--load-only",
        action="store_true",
        help="Only perform the `load` step",
    )
    parser.add_argument("environment", help="map-dev | map-qa | map-prod")
    namespace: argparse.Namespace = parser.parse_args()
    concurrency: Concurrency = get_concurrency_from_arguments(
        namespace, default=Concurrency.MULTIPROCESSING
    )
    if namespace.log:
        logging.basicConfig(filename=namespace.log, level=logging.INFO)
    if namespace.load_only:
        Broker(
            environment=namespace.environment,
            parallelism=namespace.parallelism,
            concurrency=concurrency,
            echo=namespace.echo,
        ).load()
    else:
        Broker(
            environment=namespace.environment,
            parallelism=namespace.parallelism,
            concurrency=concurrency,
            echo=namespace.echo,
        ).main()


if __name__ == "__main__":
    main()
