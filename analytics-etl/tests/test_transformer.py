import unittest
from typing import Any

from my_datastore_etl.dialects.sqlite import validate
from my_datastore_etl.transformer import Transformer as _Transformer
from sqlalchemy.orm.session import Session  # type: ignore


class Transformer(_Transformer):
    def add(self, data: Any) -> None:
        pass


class TestTransformer(unittest.TestCase):
    def test_transformer_session(self) -> None:
        transformer: Transformer = Transformer()
        session: Session = transformer.session
        validate(bind=session.bind, echo=True)


if __name__ == "__main__":
    unittest.main()
