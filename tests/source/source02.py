def echo(a):
	a = a+1
	return a

def get_pow(a):
	return a*a

def get_abs(a):
	if a>=0:
		return a
	else:
		return a*-1

def fun01(a, b):
	return get_pow(a)+get_abs(b)
