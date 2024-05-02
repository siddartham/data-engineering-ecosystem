## ChangeLog

### LakeHouse Merge Function - Spark Methods:
* Modify `Broker._spark_merge` to perform a merge into  Deltalake, then write out a copy to S3 (don't stop populating S3 tables yet).
* Modify `Broker._spark_overwrite` to perform a `copy into`  Deltalake, then write out a copy to S3 (don't stop populating S3 tables yet).

For both of the above methods—when run a job locally, as when running tests, the methods should fall back to the non-deltalake merge/overwrite functionality previously implemented.


### Lakehouse ETL Merge Function - Pandas Methods

* Implement `Broker._pandas_merge` to perform a merge into Sole Deltalake, then write out a copy to S3 (don't stop populating S3 tables yet).
* Implement `Broker._pandas_overwrite` (same as `Broker._spark_overwrite`, but for pandas Dataframes)


add [pandas module](./analytics_orm/pandas.py) and [pandas test](./tests/test_pandas.py)

For both of the above methods—when run a job locally, as when running tests, the methods should fall back to the non-deltalake merge/overwrite functionality similar to pre-deltalake Spark merge/overwrite. For both of the above methods, when not run locally, the `Work.databricks_session` should be used to connect to the Databricks warehouse.
https://github.com/nike-sustainability/nike-analytics-orm/pull/80



### Create Table Tagging Decorator in ORM

setup table tags using a decorator, similar to [how we do to create a view](./analytics_orm/view.py)(`analytics_orm.view.create_as`). This way we can enforce tagging requirements prior to deployment (force tables which are not excluded from databricks to have certain tags).

Usage syntax:

```python
from analytics.orm.tags import set_tags


@set_tags(
    techsolution="..."
)
class MyTable(Base):

    ...
```

Also, similar to what we do with views, storing the tagging data in the `Table.info` dictionary is probably best, since that lives with the table rather than the mapping class, causing it to be available in the connection's Metadata(`analytics_orm.declarative.Metadata`).

From there, we'd need to add a DDL compiler(./analytics_orm/ddl.py) and a comparator(./analytics_orm.alembic.autogenerate.py).

https://github.com/nike-sustainability/nike-analytics-orm/pull/77/files#diff-29eb6e9311d34a9d79d838f11ed0b2dac69c9b932d5641ac3b1c482f4dc61bf3

### Tweak get_bind_schema for dialect compatibility, and add get_bind_database

Change analytics_orm.utilities.get_bind_schema for dialect compatibility

In [utilities](./analytics_orm/utilities.py)

```python
def get_bind_schema(bind: Union[Connection, Engine]) -> Optional[str]:
    """
    Returns the schema set in the connection
    """
    url: sqlalchemy.engine.url.URL = bind.url
    return url.query.get("schema", None)
```

to 

```python
def get_bind_schema(bind: Union[Connection, Engine]) -> Optional[str]:
    """
    Returns the schema name from an engine or connection
    """
    url: sqlalchemy.engine.url.URL = (
        bind.engine.url if isinstance(bind, Connection) else bind.url
    )
    dialect_name: str = get_bind_dialect_name(bind)
    if dialect_name == "snowflake":
        # Snowflake appends the schema to the database name
        return (url.database or "").partition("/")[2] or None
    elif dialect_name == "sqlite":
        return None
    return url.query.get("schema", None)

def get_bind_database(bind: Union[Connection, Engine]) -> Optional[str]:
    """
    Returns the database name for an engine or connection
    """
    url: sqlalchemy.engine.url.URL = (
        bind.engine.url if isinstance(bind, Connection) else bind.url
    )
    if get_bind_dialect_name(bind) == "snowflake":
        # Snowflake appends the schema to the database name
        return (url.database or "").partition("/")[0] or None
    return url.database

```

In [validation](./analytics_orm/validation.py)

```python
    def schema(self) -> Optional[str]:
        if self.dialect_name == "sqlite":
            return None
        url: URL = cast(URL, cast(Engine, self.bind.engine).url)
        schema: Optional[str] = cast(Dict[str, str], url.query).get(
            "schema", None
        )
        if schema:
            return schema
        return (url.database or "").partition("/")[2] or None
```
to
```python
    def schema(self) -> Optional[str]:
        return get_bind_schema(self.bind)
```

In [tests](./tests/test_databricks.py)

```python
schema: str = url.query.get("schema", "default")
```
to
```python
schema: str = get_bind_schema(databricks_dev_connection) or "default"
```
https://github.com/nike-sustainability/nike-analytics-orm/pull/78/files



### Add Databricks Dialect Support

This issue covers adding minimal "databricks" dialect support to analytics-orm and simultaneously deprecating trino support.

* Deprecate trino, and while doing so—note all of the places where you've had to make changes, as many of the removals you'll need to do in reverse for databricks:
  * Remove the "trino" extra from setup.cfg 
  * Remove the trino module, all references to trino in tests, scrub trino support functions/globals from the spark, utilities, declarative, and any other modules wherein references can be found 
  * Remove all trino references from README.md 
* Add a "databricks" extra in setup.cfg, with a dependency on databricks-sql-connector. Do not specify `databricks-sql-connector[sqlalchemy]`, as Databricks has (I think unnecessarily) pinned to SQLAlchemy 2x only. The Databricks 2x requirement would conflict with `snowflake-sqlalchemy` at this time.
* Create a databricks module, implementing all of the same public functions as for snowflake (excepting any which are not applicable)
  * When not explicitly provided, infer the http_path from:
  ```python
      from pyspark.sql import SparkSession
      spark: SparkSession = SparkSession.builder.getOrCreate()
      http_path: str = (
          "sql/protocolv1/o/"
          f"{spark.sparkContext.getConf().get('spark.databricks.clusterUsageTags.orgId')}/"
          f"{spark.sparkContext.getConf().get('spark.databricks.clusterUsageTags.clusterId')}"
      )
  ```
  * When not explicitly provided, the auth token can be obtained from Cerberus in the path: "app/sustainability/ServicePrincipal.cloud.databricks.com_App.App.sustainability.Developer". Please note these creds will only work for clusters owned by the service principal—so only use when initiated from a workflow or from Airflow—when run in a notebook, you will need to create your own token and use it.


### analytics-orm validation module fails comparing  numeric types w/o precision

In this code, there's a check if the declared column type (in the model) matches what exists in the database (the "reflected" column type) and is a subclass of the sqlalchemy type 'Numeric'. If this is true, 2 more sets of checks take place: the first being that the precision of the declared type isn't None and that the declared column's precision isn't greater than the reflected column's precision.

However, if the reflected column's type is a subclass of Numeric and there is no precision, which is true of the Float (and possibly other) type, the precision comparison fails since int can't be compared to None.

 

Add a check that the precision isn't None for the reflected column type so that this check doesn't fail.

Do the same for the scale validation logic


add - `reflection_column.type.precision is not None` and `reflection_column.type.scale is not None` conditions



