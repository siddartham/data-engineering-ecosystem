import unittest

from my_datastore_orm.common_dimension import (
    AlembicVersion,
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

        assert repr(AlembicVersion()) == (
            "my_datastore_orm.common_dimension.AlembicVersion(\n"  # noqa
            "    version=None,\n"
            ")"
        )


if __name__ == "__main__":
    unittest.main()
