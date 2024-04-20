from analytics_orm.errors import TableValidationError


class NonContiguousSeasonYearCodeError(TableValidationError):
    def __repr__(self) -> str:
        return self._repr("Non-contiguous SEASON_YEAR_CODE found")


