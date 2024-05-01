from numb3rs import validate


def test_validate():
    assert validate("cat") == False
    assert validate("255.255.255.255") == True
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("1.1.1.1.1") == False
    assert validate("1.1.1.1.") == False
    assert validate("1.1.1") == False
    assert validate("ipv4 1.1.1.1") == False
