def add(a: int, b: int) -> int:
    c = a + b
    if c < 100:
        return c + 1 # This line is modified
    else:
        print("Result is too large: %d" % c)
        return -1
