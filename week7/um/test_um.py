import pytest
from um import count


def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("instrumentation") == 0
    assert count("disequilibrium") == 0
    assert count("umbilical") == 0
