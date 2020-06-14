from tests.georeum.source.source import echo, get_pow, get_abs, fun01

def test_fun01():
	assert fun01(3, 4)==13
	assert fun01(3, -4)==13
