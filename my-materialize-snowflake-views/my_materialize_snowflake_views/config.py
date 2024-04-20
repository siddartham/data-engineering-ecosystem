from typing import Dict

from analytics_etl.concurrency import Concurrency

# This is a mapping of table names to the name of a column which
# will indicate the last time a record was changed.
# The results of the query used to populate each table are compared with
# those of the existing "materialized view", and this column is updated to
# reflect the current date and time for all modified records.
TABLES_CHANGE_TRACKING_COLUMNS: Dict[str, str] = {
    "STYLE_SEASON_YEAR_SUSTAINABILITY_MV": "CHANGED"
}
DEFAULT_CONCURRENCY: Concurrency = Concurrency.FUTURES
