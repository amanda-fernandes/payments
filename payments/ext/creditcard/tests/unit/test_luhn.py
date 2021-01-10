from creditcard.luhn import Luhn


class TestLuhn:
    def test_checkdigit(self):
        assert Luhn.checkdigit('4539578763621486') is True
        assert Luhn.checkdigit('5369835519963014') is True
        assert Luhn.checkdigit('30346836403940') is True
        assert Luhn.checkdigit('3034683640394a') is False
