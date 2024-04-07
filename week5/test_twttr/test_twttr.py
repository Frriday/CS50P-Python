import pytest
from twttr import shorten

def test_twttr():
    assert shorten("aeiou") == ""
    assert shorten("twitter") == "twttr"
    assert shorten("TwittEr") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("1a2b") == "12b"
