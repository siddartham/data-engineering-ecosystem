import argparse
from enum import Enum, auto


class Concurrency(Enum):
    """
    This class enumerates the types of concurrency supported by this package,
    and is primarily used to determine the concurrency model applied to
    functions called with `analytics_etl.broker.Broker.map` and
    `analytics_etl.broker.Broker.starmap`:

    -  `analytics_etl.concurrency.Concurrency.NONE`:
       Use sequential processing (no concurrency)
    -  `analytics_etl.concurrency.Concurrency.SPARK`:
       Use Apache Spark distributed processing
    -  `analytics_etl.concurrency.Concurrency.MULTIPROCESSING`:
       Use the python `multiprocessing` module (part of the core library)
       for parallel processing
    -  `analytics_etl.concurrency.Concurrency.FUTURES`:
       Use the python `concurrent.futures` module (part of the core library)
       for parallel processing
    """

    NONE = auto()  # Sequential processing
    SPARK = auto()  # Use Apache Spark
    MULTIPROCESSING = auto()  # Use the `multiprocessing` module
    FUTURES = auto()  # Use the `concurrent.futures` module


def add_parser_concurrency_argument(
    parser: argparse.ArgumentParser,
    default: Concurrency = Concurrency.MULTIPROCESSING,
) -> None:
    """
    This function adds a `--concurrency` parameter to an argument parser for
    a Sustainability ETL package.

    Parameters:

    - parser (argparse.ArgumentParser): A parser to which we are adding the
      parameter.
    - default (analytics_etl.concurrency.Concurrency):
      This should be one of the enumerated values defined by
      `analytics_etl.concurrency.Concurrency`
    """
    parser.add_argument(
        "-c",
        "--concurrency",
        action="store",
        type=str,
        default=get_argument_value_from_concurrency(default),
        help=(
            'Which mechanism to use for parallel processing: "spark" ("s"), '
            '"multiprocessing" ("m"), "futures" ("f") or "none" ("n")'
        ),
    )


def get_concurrency_from_argument_value(
    concurrency: str, default: Concurrency = Concurrency.NONE
) -> Concurrency:
    """
    This function gets an instance of
    `analytics_etl.concurrency.Concurrency` based on a string, and
    is intended for parsing command-line input.

    Parameters:

    - concurrency (str)
    - default (analytics_etl.concurrency.Concurrency):
      This should be one of the enumerated values defined by
      `analytics_etl.concurrency.Concurrency`
    """
    if concurrency.lower().startswith("s"):
        return Concurrency.SPARK
    elif concurrency.lower().startswith("f"):
        return Concurrency.FUTURES
    elif concurrency.lower().startswith("m"):
        return Concurrency.MULTIPROCESSING
    elif concurrency.lower().startswith("n"):
        return Concurrency.NONE
    return default


def get_argument_value_from_concurrency(concurrency: Concurrency) -> str:
    """
    This function gets a string representation for an instance of
    `analytics_etl.concurrency.Concurrency`, for command-line usage.

    Parameters:

    - concurrency (analytics_etl.concurrency.Concurrency)
    """
    if concurrency == Concurrency.SPARK:
        return "spark"
    elif concurrency == Concurrency.MULTIPROCESSING:
        return "multiprocessing"
    elif concurrency == Concurrency.FUTURES:
        return "futures"
    else:
        assert concurrency == Concurrency.NONE
        return "none"


def get_concurrency_from_namespace(
    arguments: argparse.Namespace, default: Concurrency = Concurrency.NONE
) -> Concurrency:
    """
    This function determines the type of concurrency we should use based
    on parsed command-line arguments.

    Parameters:

    - arguments (argparse.Namespace)
    - default (analytics_etl.concurrency.Concurrency):
      This should be one of the enumerated values defined by
      `analytics_etl.concurrency.Concurrency`
    """
    return get_concurrency_from_argument_value(
        arguments.concurrency, default=default
    )


# for backwards compatibility
get_concurrency_from_arguments = get_concurrency_from_namespace
