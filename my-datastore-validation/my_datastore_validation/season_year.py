from datetime import datetime
from typing import Iterable, Tuple, Type

from more_itertools import first
from analytics_orm.declarative import (
    get_class_schema_name,
    get_class_table_name,
)
from analytics_orm.utilities import iter_recursive_subclasses
from my_datastore_model.base import Base
from my_datastore_model.bcl_product import SeasonYearV
from sqlalchemy.sql.expression import select  # type: ignore

from data_quality_framework.base import BaseValidation

from .errors import NonContiguousSeasonYearCodeError

SEASONS: Tuple[str, ...] = ("SP", "SU", "FA", "HO")


def _include_class(cls: Type[Base]) -> bool:
    return (
        hasattr(cls, "season_year_code")
        and (cls is not SeasonYearV)
        # Ensure the table is applicable to the bound dialect
        and bool(get_class_table_name(cls))
    )


def _get_year_and_quarter(season_year_code: str) -> Tuple[int, int]:
    season_code: str = season_year_code[:2]
    year: int = int(season_year_code[2:])
    # futureyear: int = datetime.today().year + 2
    if season_code == "SP":
        return year, 1
    elif season_code == "SU":
        return year, 2
    elif season_code == "FA":
        return year, 3
    else:
        assert season_code == "HO"
        return year, 4


class SeasonYearValidation(BaseValidation):
    def _validate_season_year_code(
        self, cls: Type[Base]
    ) -> Iterable[NonContiguousSeasonYearCodeError]:
        table_name: str = get_class_table_name(cls)
        if self.only and (table_name not in self.only):
            return
        schema: str = get_class_schema_name(cls)
        print(
            "Verifying SEASON_YEAR_CODE values are contiguous in "
            f"{table_name}"
        )
        year: int
        quarter: int
        previous_year: int = 0
        previous_quarter: int = 0
        limit_year: int = datetime.today().year + 1
        for year, quarter in sorted(
            map(
                _get_year_and_quarter,  # type: ignore
                map(
                    first,
                    self.bind.execute(select(cls.season_year_code).distinct()),
                ),
            )
        ):
            if year > limit_year:
                break
            if previous_year and previous_quarter:
                contiguous: bool
                if quarter == 1:
                    contiguous = (
                        year == previous_year + 1 and previous_quarter == 4
                    )
                else:
                    contiguous = (
                        year == previous_year
                        and previous_quarter == quarter - 1
                    )
                if not contiguous:
                    previous_season_code: str = SEASONS[quarter - 1]
                    season_code: str = SEASONS[quarter - 1]
                    yield NonContiguousSeasonYearCodeError(
                        schema=schema,
                        table_name=table_name,
                        message=(
                            "Skipped from "
                            f"{previous_season_code}{previous_year} to "
                            f"{season_code}{year}"
                        ),
                    )
            previous_year = year
            previous_quarter = quarter

    def validate(self) -> Iterable[NonContiguousSeasonYearCodeError]:
        """
        Verify that SEASON_YEAR_CODE values are contiguous for all applicable
        tables and views
        """
        # Ensure we only perform these validations for dialects
        # where SEASON_YEAR_V is applicable
        errors: Iterable[NonContiguousSeasonYearCodeError]
        for errors in map(
            self._validate_season_year_code,
            filter(_include_class, iter_recursive_subclasses(Base)),
        ):
            yield from errors
