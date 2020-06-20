from src.cover.cover import Function


def test_function():
    filepath = "/path/to/python/test.py"
    start=112
    end = 113
    name = "foo"
    func = Function(filepath, name, start, end)
    func.getHash()
    assert str(func) == f"Function '{name}' at file {filepath}: {start} - {end}"
    
    if str(func) == f"Function '{name}' at file {filepath}: {start} - {end}":
        print("If branch. This should be printed")
    else:
        print("Else branch. This should not be printed")
