from tests.georeum.source.source import echo, get_pow, get_abs, fun01


def test_echo():
    assert echo(1) == 1
    assert echo(0) == 0
    assert echo(-1) == -1
