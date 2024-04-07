from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("x/y")
        convert("4/3")
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
