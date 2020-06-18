from tests.georeum.source.source import echo, get_pow, get_abs, fun01

def test_get_abs():
	assert get_abs(4)==4
	assert get_abs(-4)==4

