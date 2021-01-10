import creditcard


class TestPackageVersion:
    def test_version(self):
        assert creditcard.__version__ == "0.0.1"
