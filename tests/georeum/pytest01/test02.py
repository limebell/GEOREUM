from tests.georeum.source.source import echo, get_pow, get_abs, fun01


def test_get_pow():
    assert get_pow(0) == 0
    assert get_pow(1) == 1
    assert get_pow(5) == 25
    assert get_pow(-2) == 4
