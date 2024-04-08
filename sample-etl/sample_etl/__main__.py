import argparse
import logging

from sample_etl.broker import Broker


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--parallelism",
        action="store",
        type=int,
        default=None,
        help=(
            "The number of Spark executors to use. If unspecified, "
            "the default number will vary based on available resources."
        ),
    )
    parser.add_argument(
        "--log",
        action="store",
        type=str,
        default=None,
        help="A local file path to for logging output.",
    )
    parser.add_argument(
        "-e",
        "--echo",
        action="store_true",
        help=(
            "This flag will cause all SQL statements, "
            "to be printed to `sys.stdout`."
        ),
    )
    parser.add_argument(
        "environment",
        help="local | test | databricks-dev | databricks-qa | databricks-prod",
        choices={
            "local",
            "test",
            "databricks-dev",
            "databricks-qa",
            "databricks-prod",
            "dev",
            "qa",
            "prod",
        },
    )
    arguments: argparse.Namespace = parser.parse_args()
    if arguments.log:
        logging.basicConfig(filename=arguments.log, level=logging.INFO)

    broker: Broker = Broker(
        environment=arguments.environment,
        parallelism=arguments.parallelism,
        echo=arguments.echo,
    )

    broker.main()


if __name__ == "__main__":
    main()
