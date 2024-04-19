"""
This script validates that there is only one head revision for each defined
environment in alembic.

Since we don't use branching in alembic, this scenario isn't desirable.
Each migration script should reference a unique `down_revision` - specifying
the same `down_revision` for multiple migrations results in a branch being
created.

https://alembic.sqlalchemy.org/en/latest/branches.html


"""

from typing import List

from alembic.config import Config  # type: ignore
from alembic.script import ScriptDirectory  # type: ignore

APPLICABLE_DIALECTS: List[str] = ["databricks", "snowflake"]
ALEMBIC_CONFIG: str = "alembic.ini"

dialect: str
for dialect in APPLICABLE_DIALECTS:
    environment: str = f"{dialect}-dev"
    config: Config = Config(ALEMBIC_CONFIG, ini_section=environment)
    script: ScriptDirectory = ScriptDirectory.from_config(config)
    heads: List[str] = script.get_heads()
    assert len(heads) <= 1, (
        f"Multiple heads found for {environment}: {heads}."
        "Please ensure that your migrations `down_revision` references the "
        "correct revision."
    )
