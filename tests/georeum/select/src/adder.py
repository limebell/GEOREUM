def add(a: int, b: int) -> int:
    c = a + b
    if c < 100:
        c = c + 1  # This line is added
        return c
    else:
        print("Result is too large: %d" % c)
        return -1
