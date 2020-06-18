from tests.georeum.source.source import echo, get_pow, get_abs, fun01

def test_echo():
	assert echo(1)==1
	assert echo(0)==0
	assert echo(-1)==-1

def test_get_pow():
	assert get_pow(0)==0
	assert get_pow(1)==1
	assert get_pow(5)==25
	assert get_pow(-2)==4

def test_get_abs():
	assert get_abs(4)==4
	assert get_abs(-4)==4

def test_fun01():
	assert fun01(3, 4)==13
	assert fun01(3, -4)==13
