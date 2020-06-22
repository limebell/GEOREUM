def add(a: int, b: int) -> int:
    c = a + b
    if c < 101:
        return c
    else:
        print("Result is too large: %d" % c)
        return -1
