from bank import value


def test_bank():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("How's going?") == 20
    assert value("What a great day") == 100
