from creditcard.utils import sanitize


class TestUtils:
    def test_sanitize(self):
        assert sanitize("4 5a 3-./!`~A|=+*&^%$#@95") == "45a3A95"
