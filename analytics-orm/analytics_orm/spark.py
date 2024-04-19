import argparse
import functools
import os
import re
import sys
from collections import OrderedDict
from dataclasses import astuple, dataclass
from datetime import datetime, timezone
from fnmatch import fnmatch
from http.client import HTTPResponse
from inspect import Traceback
from itertools import chain
from pathlib import Path
from subprocess import check_output
from typing import (
    IO,
    TYPE_CHECKING,
    AbstractSet,
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    Union,
)
from urllib.error import HTTPError
from urllib.request import urlopen
from warnings import warn
from xml.etree.ElementTree import Element

print("before lxml tree")
import lxml.etree
print("after lxml tree")
import pkg_resources
import sqlalchemy  # type: ignore
from ordered_set import OrderedSet
from pyspark import sql as pyspark_sql  # type: ignore
from pyspark.sql import SparkSession  # type: ignore
from pyspark.sql import functions as pyspark_sql_functions  # type: ignore
from pyspark.sql import types as pyspark_sql_types
from pyspark.sql.types import TimestampType  # type: ignore
from sqlalchemy.sql import sqltypes  # type: ignore

from .declarative import (
    Base,
    get_class_column_names,
    get_class_primary_key_and_column_names,
    get_class_primary_key_column_names,
)

__all__: List[str] = [
    "get_struct_type_from_mapping",
    "get_data_frame_with_unique_primary_keys",
    "merge_data_frames",
    "get_earliest_datetime",
    "get_safe_datetime",
    "add_drop_data_frame_table_columns",
    "iter_column_aligned_data_frames",
]

datetime_lru_cache: Callable[
    ..., Callable[[Callable[[], datetime]], Callable[[], datetime]]
] = functools.lru_cache  # type: ignore


@datetime_lru_cache()
def get_earliest_datetime() -> datetime:
    """
    Get the earliest datetime supported by your system when
    writing timestamps in Spark data frames.
    """
    earliest: Optional[datetime] = None
    timestamp_type: TimestampType = TimestampType()
    for timestamp in (
        -int(2**64 / 2),
        -int(2**64 / 2) + 1,
        -int(2**32 / 2),
        -int(2**32 / 2) + 1,
        -int(2**16 / 2),
        -int(2**16 / 2) + 1,
        0,
    ):
        try:
            earliest = datetime.fromtimestamp(timestamp)
            timestamp_type.toInternal(earliest)
            break
        except (OverflowError, OSError):
            if not timestamp:
                raise
    if TYPE_CHECKING:
        assert earliest
    return earliest


def get_safe_datetime(unsafe_datetime: Optional[datetime]) -> datetime:
    earliest_datetime: datetime = get_earliest_datetime()
    if not unsafe_datetime:
        return earliest_datetime
    timezone_naive_unsafe_datetime: datetime = unsafe_datetime
    if unsafe_datetime.tzinfo:
        timezone_naive_unsafe_datetime = unsafe_datetime.astimezone(
            timezone.utc
        ).replace(tzinfo=None)
    if timezone_naive_unsafe_datetime < earliest_datetime:
        return earliest_datetime
    return unsafe_datetime


def get_struct_type_from_mapping(
    mapping_class: Type[Base],
) -> pyspark_sql_types.StructType:
    """
    This function obtains an instance of `pyspark_sql_types.StructType`
    generated from a table ORM class.
    """
    assert issubclass(mapping_class, Base)
    fields: List[pyspark_sql_types.StructField] = []
    column: sqlalchemy.Column
    for column in sqlalchemy.inspect(mapping_class).columns.values():
        kwargs: Dict[str, int] = {}
        if isinstance(column.type, sqltypes.Numeric):
            if isinstance(column.type.precision, int):
                kwargs["precision"] = column.type.precision
            if isinstance(column.type.scale, int):
                kwargs["scale"] = column.type.scale
        data_type: pyspark_sql_types.DataType = (
            pyspark_sql_types.StringType()
            if isinstance(column.type, sqltypes.String)
            else (
                pyspark_sql_types.BooleanType()
                if isinstance(column.type, sqltypes.Boolean)
                else (
                    pyspark_sql_types.IntegerType()
                    if isinstance(column.type, sqltypes.Integer)
                    else (
                        pyspark_sql_types.FloatType()
                        if isinstance(column.type, sqltypes.Float)
                        else (
                            pyspark_sql_types.DecimalType(**kwargs)
                            if isinstance(column.type, sqltypes.Numeric)
                            else (
                                pyspark_sql_types.TimestampType()
                                if isinstance(column.type, sqltypes.DateTime)
                                else (
                                    pyspark_sql_types.DateType()
                                    if isinstance(column.type, sqltypes.Date)
                                    else pyspark_sql_types.NullType()
                                )
                            )
                        )
                    )
                )
            )
        )
        assert not isinstance(data_type, pyspark_sql_types.NullType)
        fields.append(
            pyspark_sql_types.StructField(
                name=column.name, dataType=data_type, nullable=column.nullable
            )
        )
    return pyspark_sql_types.StructType(fields=fields)


def get_data_frame_with_unique_primary_keys(
    data_frame: pyspark_sql.DataFrame,
    table_mapping: type,
) -> pyspark_sql.DataFrame:
    """
    This function takes a data frame and a sub-class of
    `analytics_orm.base.Base` and returns a data frame
    where there is only one record for each primary key, as defined by
    `table_mapping`. The record associated with the first use of a primary key
    is used.
    """
    assert issubclass(table_mapping, Base)
    # Get the column names, broken out by those which are and are not part
    # of the primary key
    primary_key_column_names: Tuple[str, ...]
    non_primary_key_column_names: Tuple[str, ...]
    (
        primary_key_column_names,
        non_primary_key_column_names,
    ) = get_class_primary_key_and_column_names(table_mapping)
    if non_primary_key_column_names:
        # Create a ranked data frame where the window is partitioned by
        # the primary key, and sorted by the remaining keys (granting
        # precedence to non-null values)
        return (
            data_frame.withColumn(
                "_row_number",
                pyspark_sql_functions.row_number().over(
                    pyspark_sql.Window.partitionBy(
                        *primary_key_column_names
                    ).orderBy(
                        *(
                            pyspark_sql_functions.asc_nulls_last(column_name)
                            for column_name in non_primary_key_column_names
                        )
                    )
                ),
            )
            .filter("_row_number = 1")
            .drop("_row_number")
        )
    return data_frame.distinct()


def add_drop_data_frame_table_columns(
    data_frame: pyspark_sql.DataFrame,
    table_mapping: Optional[Type[Base]] = None,
    columns: Iterable[str] = (),
    defaults: Optional[Dict[str, Any]] = None,
) -> pyspark_sql.DataFrame:
    """
    Add and/or drop columns from the provided data frame to align with the
    indicated table class (or a provided tuple of column names).

    Parameters:

    - data_frame (pyspark.sql.DataFrame)
    - table_mapping (type|None) = None
    - columns ((str,)) = ()
    - defaults ({str: typing.Any}|None) = None
    """
    assert table_mapping or columns
    if table_mapping and not columns:
        columns = get_class_column_names(table_mapping)
    if not isinstance(columns, AbstractSet):
        columns = OrderedSet(columns)
    data_frame_columns: AbstractSet[str] = OrderedSet(data_frame.columns)
    column: str
    for column in columns - data_frame_columns:
        default: Any = None
        if defaults:
            default = defaults.get(column, None)
        data_frame = data_frame.withColumn(
            column, pyspark_sql_functions.lit(default)
        )
    for column in data_frame_columns - columns:
        data_frame = data_frame.drop(column)
    return data_frame


def iter_column_aligned_data_frames(
    data_frames: Iterable[pyspark_sql.DataFrame],
    defaults: Optional[Dict[str, Any]] = None,
) -> Iterable[pyspark_sql.DataFrame]:
    """
    Append columns as needed to data frames such that all have the same
    columns (by name).

    Parameters:

    - data_frames ([pyspark.sql.DataFrame]): One or more data frames
    - defaults ({str: typing.Any}|None) = None: A mapping of column
      names to default values to fill in when/if adding columns.
    """
    data_frames = tuple(data_frames)
    columns: OrderedSet[str] = OrderedSet()
    data_frame: pyspark_sql.DataFrame
    for data_frame in data_frames:
        columns |= OrderedSet(data_frame.columns)
    for data_frame in data_frames:
        if columns - set(data_frame.columns):
            yield add_drop_data_frame_table_columns(
                data_frame,
                columns=columns,
                defaults=defaults,
            )
        else:
            yield data_frame


def merge_data_frames(
    data_frames: Iterable[pyspark_sql.DataFrame],
    table_mapping: Optional[Type[Base]] = None,
    primary_key: Tuple[str, ...] = (),
    defaults: Optional[Dict[str, Any]] = None,
) -> pyspark_sql.DataFrame:
    """
    This function takes two or more data frames and a sub-class of
    `analytics_orm.base.Base` and returns a data frame
    wherein a record associated with each primary key is sourced only from the
    first data frame in which it is encountered.

    Parameters:

    - data_frames ([pyspark.sql.DataFrame])
    - table_mapping (type|None) = None: A table from which to infer a primary
      key.
    - primary_key ((str,)) = (): A tuple of strings representing the names
      of the primary key columns.
    - defaults ({str: typing.Any}|None) = None: A mapping of column
      names to default values to fill in when/if adding columns.
    """
    if not primary_key:
        if not (
            isinstance(table_mapping, type) and issubclass(table_mapping, Base)
        ):
            raise ValueError(repr(locals()))
        primary_key = get_class_primary_key_column_names(table_mapping)
    data_frame: pyspark_sql.DataFrame
    # Ensure all data frames have matching columns (by name)
    if table_mapping:
        # If a table mapping class was provided, use the table's columns
        data_frames = map(
            lambda data_frame: add_drop_data_frame_table_columns(
                data_frame,
                table_mapping=table_mapping,
                defaults=defaults,
            ),
            data_frames,
        )
    else:
        # If a table mapping class was not provided, expand input data
        # frames to include all columns
        data_frames = iter_column_aligned_data_frames(
            data_frames,
            defaults=defaults,
        )
    ordinal: int
    unified_data_frame: Optional[pyspark_sql.DataFrame] = None
    for ordinal, data_frame in enumerate(data_frames, 1):
        data_frame = data_frame.withColumn(
            "_data_frame_ordinal", pyspark_sql_functions.lit(ordinal)
        )
        if unified_data_frame is None:
            unified_data_frame = data_frame
        else:
            unified_data_frame = unified_data_frame.unionByName(data_frame)
    if TYPE_CHECKING:
        assert unified_data_frame is not None
    return (
        unified_data_frame.withColumn(
            "_window_row_number",
            pyspark_sql_functions.row_number().over(
                pyspark_sql.Window.partitionBy(*primary_key).orderBy(
                    "_data_frame_ordinal"
                )
            ),
        )
        .filter("_window_row_number = 1")
        .drop("_window_row_number")
        .drop("_data_frame_ordinal")
    )


lru_cache: Callable[..., Any] = functools.lru_cache


DELTA_PRE_RELEASE_MAVEN_ROOT: str = (
    "https://oss.sonatype.org/content/repositories/iodelta-1133/"
)
MAVEN_ROOT: str = "https://repo1.maven.org/maven2/"
TRINO_JDBC: str = "io.trino:trino-jdbc"
SNOWFLAKE_JDBC: str = "net.snowflake:snowflake-jdbc"
DATABRICKS_JDBC: str = "com.databricks:databricks-jdbc"
DELTA_CORE: str = "io.delta:delta-core_*"
DELTA_SPARK: str = "io.delta:delta-spark_*"
SCALA_LIBRARY: str = "org.scala-lang:scala-library"


@lru_cache()
def get_spark_home() -> str:
    spark_home: str = check_output(
        [sys.executable, "-W", "ignore", "-m", "pyspark.find_spark_home"],
        encoding="utf-8",
        universal_newlines=True,
    )
    print(f"Spark Home: {spark_home}")
    return spark_home.strip()


def _get_version_tuple(version: str) -> Tuple[int, ...]:
    return tuple(int(version_part) for version_part in version.split("."))


@lru_cache()
def _get_latest_maven_compatible_repo_version(
    name: str,
    major_version: int,
    maven_artifacts_root: str = MAVEN_ROOT,
) -> str:
    """
    Get the HADOOP version pyspark will use
    """

    def major_version_filter_function(version: Tuple[int, ...]) -> bool:
        return version[0] == major_version

    return _get_latest_maven_repo_version(
        name,
        filter_function=major_version_filter_function,
        maven_artifacts_root=maven_artifacts_root,
    )


def _iter_links(url: str) -> Iterable[str]:
    http_response: HTTPResponse
    with urlopen(url) as http_response:
        html: str = str(http_response.read(), encoding="utf-8")
        maven_artifacts_root: Element = lxml.etree.HTML(html)  # type: ignore
    element: Element
    for element in maven_artifacts_root.findall(".//a"):
        if element.attrib.get("href", ""):
            yield element.attrib["href"]


def _iter_maven_jar_versions(
    identifier: str, maven_artifacts_root: str = MAVEN_ROOT
) -> Iterable[str]:
    """
    Iterate over all versions available for the indicated package
    """
    path: str = _parse_maven_package_identifier(identifier).path
    href: str
    for href in _iter_links(f"{maven_artifacts_root}{path}/"):
        if re.match(r"^[\d.]*[\d]/$", href):
            yield href.rstrip("/")


def _has_pattern(name: str) -> bool:
    return bool(name and set("*[?") & set(name))


def _any_version_filter_function(version: Tuple[int, ...]) -> bool:
    return True


def _get_version_filter_function(pattern: str) -> Callable[[str], bool]:
    def filter_function(version: str) -> bool:
        return fnmatch(version, pattern)

    return filter_function


@lru_cache()
def _get_latest_maven_repo_version(
    name: str,
    version: str = "",
    maven_artifacts_root: str = MAVEN_ROOT,
) -> str:
    """
    Find the latest version of a jar.

    - version (str) = "": An (optional) glob pattern. If provided, only
      versions matching this pattern will be considered.
    """
    pattern: str
    filter_function: Callable[[str], bool] = lambda pattern: True
    if version:
        filter_function = _get_version_filter_function(version)
    versions: Tuple[Tuple[int, ...], ...] = tuple(
        map(
            _get_version_tuple,
            filter(
                filter_function,
                _iter_maven_jar_versions(name, maven_artifacts_root),
            ),
        )
    )
    if not versions:
        raise ValueError(f'No versions matching "{version}" were found')
    return ".".join(str(version_int) for version_int in max(versions))


@lru_cache()
def get_spark_conf_directory() -> str:
    path: str = f"{get_spark_home()}/conf"
    os.makedirs(path, exist_ok=True)
    return f"{path}/"


def _line_is_not_empty(line: str) -> bool:
    return True if line.strip() else False


class SparkDefaults:
    __slots__ = ("_dict",)

    def __init__(self) -> None:
        self._dict: Dict[str, Set[str]] = OrderedDict()

    def __getitem__(self, key: str) -> Set[str]:
        values: Set[str] = self._dict.get(key, set())
        self._dict[key] = values
        return values

    def __setitem__(self, key: str, values: Union[Iterable[str], str]) -> None:
        if not isinstance(values, set):
            if isinstance(values, str):
                values = {values}
            else:
                assert isinstance(values, Iterable)
                values = set(values)
        self._dict[key] = values

    def __enter__(self) -> "SparkDefaults":
        file_io: IO[str]
        try:
            with open(
                f"{get_spark_conf_directory()}spark-defaults.conf", "r"
            ) as file_io:
                line: str
                for line in filter(_line_is_not_empty, file_io.readlines()):
                    key: str
                    value: str
                    key, value = re.split(r"\s+", line.strip(), maxsplit=1)
                    self[key].add(value)
        except FileNotFoundError:
            pass
        return self

    def _iter_lines(self) -> Iterable[str]:
        key: str
        values: Set[str]
        if self._dict:
            column_width: int = max(len(key) for key in self._dict.keys()) + 1
            for key, values in self._dict.items():
                if values:
                    yield (
                        f"{key}{' ' * (column_width - len(key))}"
                        f"{','.join(sorted(values))}\n"
                    )
            yield ""

    def __exit__(
        self, type_: type, value: Exception, traceback: Traceback
    ) -> None:
        with open(
            f"{get_spark_conf_directory()}spark-defaults.conf",
            "w",
        ) as file_io:
            file_io.writelines(self._iter_lines())

    def clear(self) -> None:
        key: str
        values: Set[str]
        for key, values in self._dict.items():
            values.clear()

    def items(self) -> Iterable[Tuple[str, Iterable[str]]]:
        for key, values in self._dict.items():
            if values:
                yield key, sorted(values)


@dataclass
class _MavenPackage:
    identifier: str
    path: str
    qualified_name: str
    version: str


def _parse_maven_package_identifier(identifier: str) -> _MavenPackage:
    return next(iter(_iter_maven_packages(identifier)))


@lru_cache()
def get_maven_package_url(
    identifier: str, maven_artifacts_root: str = MAVEN_ROOT
) -> str:
    """
    Get the URL of the latest version of a Maven package, by identifier. If
    there are unix-style (glob) wildcards in the package name, all matching
    packages will be searched.

    Parameters:

    - identifier (str): A Maven package identifier, potentially including
      wildcards in the package name (but not in the org name)

    See [fnmatch](https://docs.python.org/3/library/fnmatch.html) for pattern
    matching syntax.
    """
    maven_package: _MavenPackage
    # A dictionary mapping latest versions to identifiers
    latest_versions_urls: Dict[Tuple[int, ...], str] = {}
    for maven_package in _iter_maven_packages(identifier):
        version: str = maven_package.version
        if _has_pattern(version) or not version:
            version = _get_latest_maven_repo_version(
                maven_package.identifier,
                version,
                maven_artifacts_root=maven_artifacts_root,
            )
        if version:
            url: str = (
                f"{maven_artifacts_root}{maven_package.path}/{version}/"
                f"{maven_package.qualified_name.rpartition(':')[-1]}"
                f"-{version}.jar"
            )
            try:
                # Check to see if the URL exists
                urlopen(url)
                # If there was no error in opening the URL, we map it to the
                # URL
                latest_versions_urls[_get_version_tuple(version)] = url
            except HTTPError as error:
                if error.code != 404:
                    raise
                warn(f"{url} not found")
    if not latest_versions_urls:
        raise ValueError(
            f'A Maven package matching "{identifier}" could not be found in '
            f"{maven_artifacts_root}"
        )
    # Return the highest of all the "latest" versions found in all matched
    # packages
    return latest_versions_urls[max(latest_versions_urls.keys())]


def _iter_maven_packages(
    identifier: str, maven_artifacts_root: str = MAVEN_ROOT
) -> Iterable[_MavenPackage]:
    """
    Iterate over matching Maven package identifiers
    """
    part: str
    parts: List[str] = identifier.split(":")
    version: str = ""
    if len(parts) > 2:
        version = parts.pop()
    name: str = parts[-1]
    if _has_pattern(name):
        # If a glob pattern is found in the package name,
        # find all matching packages
        assert len(parts) > 1
        parent_path: str = "/".join(
            map(lambda part: part.replace(".", "/"), parts[:-1])
        )
        href: str
        for href in _iter_links(f"{maven_artifacts_root}{parent_path}/"):
            href_name: str = href.rstrip("/")
            if fnmatch(href_name, name):
                assert not _has_pattern(href_name)
                maven_package: _MavenPackage
                href_identifier: str = f"{':'.join(parts[:-1])}:{href_name}"
                if version:
                    href_identifier = f"{href_identifier}:{version}"
                yield from _iter_maven_packages(href_identifier)
    else:
        qualified_name: str = ":".join(parts)
        path: str = parts[0].replace(".", "/")
        if len(parts) > 1:
            path = f"{path}/{'/'.join(parts[1:])}"
        if _has_pattern(version):
            try:
                version = _get_latest_maven_repo_version(
                    qualified_name,
                    version=version,
                    maven_artifacts_root=maven_artifacts_root,
                )
            except ValueError:
                return
        yield _MavenPackage(
            identifier,
            path,
            qualified_name,
            version,
        )


def _add_jar_package_to_spark_defaults(
    identifier: str,
    spark_defaults: SparkDefaults,
    maven_artifacts_root: str = MAVEN_ROOT,
) -> None:
    repository_path: str
    version: str
    identifier, repository_path, qualified_name, version = astuple(
        _parse_maven_package_identifier(identifier)
    )
    if version == "latest" or not version:
        version = _get_latest_maven_repo_version(
            qualified_name, maven_artifacts_root=maven_artifacts_root
        )

    def _is_version_of_package(variant_identifier: str) -> bool:
        return (
            _parse_maven_package_identifier(variant_identifier).qualified_name
            == qualified_name
        )

    file_name: str
    packages_str: str
    spark_jars_packages: Set[str] = set(
        chain(
            *(
                packages_str.split(",")
                for packages_str in spark_defaults["spark.jars.packages"]
            )
        )
    )
    spark_jars_packages.difference_update(
        set(
            filter(
                _is_version_of_package,
                spark_jars_packages,
            )
        )
    )
    spark_jars_packages.add(f"{qualified_name}:{version}")
    spark_defaults["spark.jars.packages"].clear()
    spark_defaults["spark.jars.packages"].update(spark_jars_packages)


def _remove_jar_package_from_spark_defaults(
    pattern: str, spark_defaults: SparkDefaults
) -> None:
    name: str
    packages_str: str
    spark_jars_packages: Set[str] = set(
        filter(
            lambda name: not fnmatch(name, pattern),
            chain(
                *(
                    packages_str.split(",")
                    for packages_str in spark_defaults["spark.jars.packages"]
                )
            ),
        )
    )
    spark_defaults["spark.jars.packages"].clear()
    spark_defaults["spark.jars.packages"].update(spark_jars_packages)


def _add_driver_extra_class_path_to_spark_defaults(
    path: str, spark_defaults: SparkDefaults
) -> None:
    jars_str: str
    spark_jars: Set[str] = set(
        chain(
            *(
                jars_str.split(",")
                for jars_str in spark_defaults["spark.driver.extraClassPath"]
            )
        )
    )
    spark_jars.add(path)
    spark_defaults["spark.driver.extraClassPath"].clear()
    spark_defaults["spark.driver.extraClassPath"].update(spark_jars)


def _remove_driver_extra_class_path_from_spark_defaults(
    pattern: str, spark_defaults: SparkDefaults
) -> None:
    jars_str: str
    path: str
    spark_jars: Set[str] = set(
        filter(
            lambda path: not fnmatch(path.rpartition("/")[-1], pattern),
            chain(
                *(
                    jars_str.split(",")
                    for jars_str in spark_defaults[
                        "spark.driver.extraClassPath"
                    ]
                )
            ),
        )
    )
    spark_defaults["spark.driver.extraClassPath"].clear()
    spark_defaults["spark.driver.extraClassPath"].update(spark_jars)


@lru_cache()
def _iter_ivy_directories() -> Iterable[Path]:
    path: Path
    yield from map(
        Path,
        filter(
            os.path.exists,
            (
                (
                    SparkSession.builder.getOrCreate()
                    .sparkContext.getConf()
                    .get("spark.jars.ivy", "")
                ),
                os.path.expanduser("~/.ivy2"),
                "/tmp/.ivy2",
                os.path.join(get_spark_home(), ".ivy2"),
            ),
        ),
    )


@lru_cache()
def _get_jar_path(package_identifier: str, maven_artifacts_root: str = MAVEN_ROOT) -> Path:
    """
    Download, or return the path of if already downloaded, the JAR for
    the identified package.
    """
    # If no jar was found, download it manually and return the path
    url: str = get_maven_package_url(
        package_identifier, maven_artifacts_root=maven_artifacts_root
    )
    file_name: str = url.rpartition("/")[-1]
    path: Path = Path(get_spark_home()).joinpath("jars", file_name).absolute()
    data: bytes
    with urlopen(url) as read_io:
        data = read_io.read()
    with open(path, "wb") as write_io:
        write_io.write(data)
    return path


def install_trino_jars() -> None:
    """
    This function updates Spark Defaults to retrieve and use a driver for Trino
    databases.
    """
    with SparkDefaults() as spark_defaults:
        _add_jar_package_to_spark_defaults(TRINO_JDBC, spark_defaults)
        _add_driver_extra_class_path_to_spark_defaults(
            str(_get_jar_path(TRINO_JDBC)), spark_defaults
        )
    print("Success!")


def _get_delta_core_scala_library_version(identifier: str) -> str:
    maven_package_url: str = get_maven_package_url(identifier)
    matched: Optional[re.Match] = re.search(
        r"delta-core_([\d.]+)-", maven_package_url
    )
    if matched:
        return matched.groups()[0]
    return ""


def install_delta_core(version: str = "") -> None:
    """
    This function updates Spark Defaults to retrieve and use the Delta Lake
    Spark extension

    Parameters:

    - version (str) = ""
    """
    identifier: str = DELTA_CORE
    if not version:
        # Select the highest compatible version
        # https://docs.delta.io/latest/releases.html
        pyspark_version: str = pkg_resources.get_distribution(
            "pyspark"
        ).version
        if pyspark_version.startswith("3.0."):
            version = "0.8.*"
        elif pyspark_version.startswith("3.1."):
            version = "1.0.*"
        elif pyspark_version.startswith("3.2."):
            version = "2.0.*"
        elif pyspark_version.startswith("3.3."):
            version = "2.2.*"
    if version:
        identifier = f"{identifier}:{version}"
    scala_library_identifier: str = SCALA_LIBRARY
    scala_library_version: str = _get_delta_core_scala_library_version(
        identifier
    )
    if scala_library_version:
        scala_library_identifier = (
            f"{scala_library_identifier}:{scala_library_version}.*"
        )
    with SparkDefaults() as spark_defaults:
        _remove_driver_extra_class_path_from_spark_defaults(
            "*delta*", spark_defaults
        )
        _remove_driver_extra_class_path_from_spark_defaults(
            "*scala*", spark_defaults
        )
        _remove_jar_package_from_spark_defaults("*delta*", spark_defaults)
        _remove_jar_package_from_spark_defaults("*scala*", spark_defaults)
        _add_jar_package_to_spark_defaults(
            scala_library_identifier, spark_defaults
        )
        _add_jar_package_to_spark_defaults(identifier, spark_defaults)
        _add_driver_extra_class_path_to_spark_defaults(
            str(_get_jar_path(scala_library_identifier)), spark_defaults
        )
        _add_driver_extra_class_path_to_spark_defaults(
            str(_get_jar_path(identifier)), spark_defaults
        )
        spark_defaults["spark.sql.extensions"].add(
            "io.delta.sql.DeltaSparkSessionExtension"
        )
        spark_defaults["spark.sql.catalog.spark_catalog"].add(
            "org.apache.spark.sql.delta.catalog.DeltaCatalog"
        )
    print("Success!")


def install_snowflake_jars(version: str = "") -> None:
    """
    This function updates Spark Defaults to retrieve and use a driver for
    Snowflake databases.
    """
    identifier: str = SNOWFLAKE_JDBC
    if version:
        identifier = f"{identifier}:{version}"
    with SparkDefaults() as spark_defaults:
        _add_jar_package_to_spark_defaults(
            identifier, spark_defaults, maven_artifacts_root=MAVEN_ROOT
        )
        _add_driver_extra_class_path_to_spark_defaults(
            str(_get_jar_path(identifier, maven_artifacts_root=MAVEN_ROOT)),
            spark_defaults,
        )
    print("Success!")


def install_databricks_jars(version: str = "") -> None:
    """
    This function updates Spark Defaults to retrieve and use a driver for
    Databricks databases.
    """
    identifier: str = DATABRICKS_JDBC
    if version:
        identifier = f"{identifier}:{version}"
    with SparkDefaults() as spark_defaults:
        _add_jar_package_to_spark_defaults(
            identifier, spark_defaults, maven_artifacts_root=MAVEN_ROOT
        )
        _add_driver_extra_class_path_to_spark_defaults(
            str(_get_jar_path(identifier, maven_artifacts_root=MAVEN_ROOT)),
            spark_defaults,
        )
    print("Success!")

def _print_help() -> None:
    print(
        "Usage:\n"
        "  analytics-orm spark <command> [options]\n\n"
        "Commands:\n"
        "  install-trino-jdbc-driver\n"
        "                              Configure Spark to load and use a "
        "Trino JDBC driver\n"
        "  install-snowflake-jdbc-driver\n"
        "                              Configure Spark to load and use a "
        "Snowflake JDBC driver"
    )


def _get_command() -> str:
    command: str = ""
    if len(sys.argv) > 1:
        command = sys.argv.pop(1)
    return command


def main() -> None:
    """
    This function is the CLI entry point for the following commands:

    - `analytics-orm spark install-trino-jdbc-driver`
    - `analytics-orm spark install-snowflake-jdbc-driver`
    - `analytics-orm spark install-delta-core`
    """
    command = _get_command()
    if command in ("-h", "--help"):
        _print_help()
    elif command in ("install-trino-jdbc-driver", "get-trino-jdbc-driver"):
        argparse.ArgumentParser(
            prog="analytics-orm spark install-trino-jdbc-driver",
            description=(
                "Configure Spark to load and use a Trino JDBC driver"
            ),
        ).parse_args()
        install_trino_jars()
    elif command in (
        "install-snowflake-jdbc-driver",
        "get-snowflake-jdbc-driver",
    ):
        argparse.ArgumentParser(
            prog="nike-analytics-orm spark install-snowflake-jdbc-driver",
            description=(
                "Configure Spark to load and use a Snowflake JDBC driver"
            ),
        ).parse_args()
        install_snowflake_jars()
    elif command == "install-delta-core":
        parser: argparse.ArgumentParser = argparse.ArgumentParser(
            prog="analytics-orm spark install-delta-core",
            description=(
                "Configure Spark to load and use the Delta Lake extension"
            ),
        )
        parser.add_argument(
            "-v",
            "--version",
            default="",
            help=(
                "The version of Delta Lake to use. See the "
                "[release compatibility matrix]"
                "(https://docs.delta.io/latest/releases.html) for more "
                "information."
            ),
        )
        namespace: argparse.Namespace = parser.parse_args()
        install_databricks_jars(namespace.version)
    else:
        _print_help()
        raise ValueError(command)


if __name__ == "__main__":
    main()
