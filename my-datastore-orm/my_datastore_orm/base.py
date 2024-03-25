"""
This module defines a declarative base and common types for all models in this
library
"""

import importlib
from typing import Any

from orm_framework import declarative
from sqlalchemy import Numeric  # type: ignore

Base: Any = declarative.declarative_base()
NUMERIC = Numeric(38, 4)
# This causes all schemas to be loaded
importlib.import_module(".".join(__name__.split(".")[:-1]))
