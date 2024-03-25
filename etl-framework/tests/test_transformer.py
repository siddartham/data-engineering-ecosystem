import unittest
from typing import Any

from my_datastore_etl_wrapper.transformer import Transformer as _Transformer
from my_datastore_.dialects.sqlite import validate
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
