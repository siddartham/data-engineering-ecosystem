from types import ModuleType
from typing import List, Optional

from . import autogenerate, ddl, migrations, operations

databricks: Optional[ModuleType]
try:
    from . import databricks
except ImportError:
    databricks = None
snowflake: Optional[ModuleType]
try:
    from . import snowflake
except ImportError:
    snowflake = None

__all__: List[str] = [
    "autogenerate",
    "operations",
    "ddl",
    "migrations",
    "snowflake",
    "databricks",
]
