from typing import Any, Type

from analytics_etl.transformer import Transformer as _Transformer
from analytics_orm.declarative import Base as ORMBase
from my_datastore_model.base import Base


class Transformer(_Transformer):

    def __init__(
        self,
        data: Any = None,
        echo: bool = False,
        base: Type[ORMBase] = Base,
    ) -> None:
        super().__init__(data=data, echo=echo, base=base)
