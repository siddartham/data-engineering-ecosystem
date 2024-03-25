import unittest

from my_datastore_orm.fnd_common import (
    EnablonIngressConversion,
)


class TestBroker(unittest.TestCase):
    """
    TODO
    """

    def test_repr(self) -> None:
        """
        Verify that `my_datastore_orm.base.Base.__repr__()`
        returns the expected value when called by a sub-class.
        """

        assert repr(EnablonIngressConversion()) == (
            "my_datastore_orm.common_dimention.AlembicVersion(\n"  # noqa
            "    version=None,\n"
            ")"
        )


if __name__ == "__main__":
    unittest.main()
