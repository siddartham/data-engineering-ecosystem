import argparse
import logging
import sys
from multiprocessing.pool import Pool
from typing import Iterable, Tuple, Union

from . import experimental, v1
from ._utilities import (
    get_client,
    iter_client_file_dag_ids,
    pause_experimental_client_dag,
    pause_v1_client_dag,
    run_experimental_client_dag,
    run_v1_client_dag,
    unpause_experimental_client_dag,
    unpause_v1_client_dag,
)


def _print_help() -> None:
    print(
        "Usage:\n"
        "  map-airflow-client <command> [options]\n\n"
        "Commands:\n"
        "  run                         Trigger a DAG run.\n"
        "  pause                       Pause a DAG.\n"
        "  unpause                     Un-pause a DAG.\n"
        "  create-connection           Create a connection.\n"
        "  delete-connection           Delete a connection."
    )


def _get_command() -> str:
    command: str = ""
    if len(sys.argv) > 1:
        command = sys.argv.pop(1)
    return command


def _add_client_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-cn",
        "--cluster-name",
        type=str,
        action="store",
        default="",
        help="The name of your MAP cluster.",
    )
    parser.add_argument(
        "-r",
        "--region",
        type=str,
        action="store",
        default="",
        help="Your MAP cluster's AWS region: us-west-2 | us-east-1 | etc.",
    )
    parser.add_argument(
        "-cid",
        "--client-id",
        type=str,
        action="store",
        default="",
        help="Your OAuth2 client ID.",
    )
    parser.add_argument(
        "-cs",
        "--client-secret",
        type=str,
        action="store",
        default="",
        help="Your OAuth2 client secret.",
    )
    parser.add_argument(
        "-cscp",
        "--client-secret-cerberus-path",
        type=str,
        action="store",
        default="",
        help=(
            "A Cerberus secure data path where your OAuth2 client secret "
            "is stored."
        ),
    )
    parser.add_argument(
        "-l",
        "--log",
        action="store",
        type=str,
        default="",
        help="Log output path",
    )
    parser.add_argument(
        "-e",
        "--echo",
        action="store_const",
        const=True,
        default=False,
        help="Echo requests/responses",
    )


def _add_dag_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-did",
        "--dag-id",
        type=str,
        action="append",
        default=[],
        help="The ID of one or more DAGs to run.",
    )
    parser.add_argument(
        "-dfn",
        "--dag-file-name",
        type=str,
        action="append",
        default=[],
        help=(
            "The file name of one or more DAGs. Please note that this "
            "argument is only valid for use with clusters using Airflow "
            "version 2 or later. For Airflow version 1 MAP clusters, "
            "please provide DAG IDs using the `--dag-id` parameter."
        ),
    )


def _parse_pause_arguments() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="map-airflow-client pause", description="Pause DAG(s)."
    )
    _add_client_arguments(parser)
    _add_dag_arguments(parser)
    return parser.parse_args()


def _parse_unpause_arguments() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="map-airflow-client unpause", description="Un-pause DAG(s)."
    )
    _add_client_arguments(parser)
    _add_dag_arguments(parser)
    return parser.parse_args()


def _parse_run_arguments() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="map-airflow-client run", description="Trigger a DAG run."
    )
    _add_client_arguments(parser)
    _add_dag_arguments(parser)
    parser.add_argument(
        "-d",
        "--detach",
        action="store_const",
        const=True,
        default=False,
        help=(
            "Detached mode: Do not wait for the DAG run to finish. Please "
            "only use this flag if you do not need to ensure the successful "
            "completion of the triggered DAG run, as detached mode does not "
            "wait to verify successful completion of the run prior to exit."
        ),
    )
    return parser.parse_args()


def _get_namespace_client(
    namespace: argparse.Namespace,
) -> Union[v1.client.Client, experimental.client.Client]:
    return get_client(
        cluster_name=namespace.cluster_name,
        region=namespace.region,
        client_id=namespace.client_id,
        client_secret=namespace.client_secret,
        client_secret_cerberus_path=namespace.client_secret_cerberus_path,
        echo=namespace.echo,
    )


def _get_client_namespace_dag_ids(
    client: Union[v1.client.Client, experimental.client.Client],
    namespace: argparse.Namespace,
) -> Tuple[str, ...]:
    return (tuple(namespace.dag_id) if namespace.dag_id else ()) + (
        tuple(iter_client_file_dag_ids(client, namespace.dag_file_name))
        if namespace.dag_file_name
        else ()
    )


def run() -> None:
    namespace: argparse.Namespace = _parse_run_arguments()
    if namespace.log:
        logging.basicConfig(filename=namespace.log, level=logging.INFO)
    client: Union[
        v1.client.Client, experimental.client.Client
    ] = _get_namespace_client(namespace)
    dag_ids: Tuple[str, ...] = _get_client_namespace_dag_ids(client, namespace)
    dag_ids_length: int = len(dag_ids)
    arguments: Iterable[
        Tuple[Union[v1.client.Client, experimental.client.Client], str, bool]
    ] = zip(
        (client,) * dag_ids_length,
        dag_ids,
        (namespace.detach,) * dag_ids_length,
    )
    pool: Pool = Pool()
    if isinstance(client, v1.client.Client):
        pool.starmap(run_v1_client_dag, arguments)
    else:
        pool.starmap(run_experimental_client_dag, arguments)


def pause() -> None:
    namespace: argparse.Namespace = _parse_pause_arguments()
    if namespace.log:
        logging.basicConfig(filename=namespace.log, level=logging.INFO)
    client: Union[
        v1.client.Client, experimental.client.Client
    ] = _get_namespace_client(namespace)
    dag_ids: Tuple[str, ...] = _get_client_namespace_dag_ids(client, namespace)
    pool: Pool = Pool()
    if isinstance(client, v1.client.Client):
        pool.starmap(
            pause_v1_client_dag, zip((client,) * len(dag_ids), dag_ids)
        )
    else:
        pool.starmap(
            pause_experimental_client_dag,
            zip((client,) * len(dag_ids), dag_ids),
        )


def unpause() -> None:
    namespace: argparse.Namespace = _parse_unpause_arguments()
    if namespace.log:
        logging.basicConfig(filename=namespace.log, level=logging.INFO)
    client: Union[
        v1.client.Client, experimental.client.Client
    ] = _get_namespace_client(namespace)
    dag_ids: Tuple[str, ...] = _get_client_namespace_dag_ids(client, namespace)
    pool: Pool = Pool()
    if isinstance(client, v1.client.Client):
        pool.starmap(
            unpause_v1_client_dag, zip((client,) * len(dag_ids), dag_ids)
        )
    else:
        pool.starmap(
            unpause_experimental_client_dag,
            zip((client,) * len(dag_ids), dag_ids),
        )


def _add_create_connection_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--connection-id",
        action="store",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--connection-type",
        action="store",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--description",
        action="store",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--host",
        action="store",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--login",
        action="store",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--schema",
        action="store",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--port",
        action="store",
        type=int,
        default=None,
    )
    parser.add_argument(
        "--password",
        action="store",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--extra",
        action="store",
        type=str,
        default=None,
    )


def _parse_create_connection_arguments() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="map-airflow-client create-connection",
        description="Create or update a connection",
    )
    _add_client_arguments(parser)
    _add_create_connection_arguments(parser)
    return parser.parse_args()


def create_connection() -> None:
    namespace: argparse.Namespace = _parse_create_connection_arguments()
    if namespace.log:
        logging.basicConfig(filename=namespace.log, level=logging.INFO)
    client: Union[
        v1.client.Client, experimental.client.Client
    ] = _get_namespace_client(namespace)
    if isinstance(client, experimental.client.Client):
        raise NotImplementedError(
            'This operation is not supported for the "experimental" rest API'
        )
    assert namespace.connection_id
    connection: v1.model.Connection = v1.model.Connection(
        connection_id=namespace.connection_id,
        conn_type=namespace.connection_type,
        # `description` only implemented in future versions
        # description=namespace.description,
        host=namespace.host,
        login=namespace.login,
        schema=namespace.schema,
        port=namespace.port,
        password=namespace.password,
        extra=namespace.extra,
    )
    try:
        client.patch_connections_connection_id(
            connection=connection,
            connection_id=namespace.connection_id,
        )
    except Exception:
        client.post_connections(connection)


def _parse_delete_connection_arguments() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="map-airflow-client delete-connection",
        description="Delete a connection",
    )
    _add_client_arguments(parser)
    parser.add_argument(
        "--connection-id",
        action="store",
        type=str,
        default=None,
    )
    return parser.parse_args()


def delete_connection() -> None:
    namespace: argparse.Namespace = _parse_delete_connection_arguments()
    if namespace.log:
        logging.basicConfig(filename=namespace.log, level=logging.INFO)
    client: Union[
        v1.client.Client, experimental.client.Client
    ] = _get_namespace_client(namespace)
    if isinstance(client, experimental.client.Client):
        raise NotImplementedError(
            'This operation is not supported for the "experimental" rest API'
        )
    assert namespace.connection_id
    client.delete_connections_connection_id(namespace.connection_id)


def main() -> None:
    command = _get_command()
    if command == "run":
        run()
    elif command == "pause":
        pause()
    elif command == "unpause":
        unpause()
    elif command == "create-connection":
        create_connection()
    elif command == "delete-connection":
        delete_connection()
    else:
        _print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
