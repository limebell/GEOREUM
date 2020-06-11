from src.cover.cover import Line

def test_line():
    filepath = "/path/to/python/test.py"
    line_no = 112
    line_text = "def foo():\n"
    line = Line(filepath, line_no, line_text)
    assert str(line) ==  line_text[:-1]
    assert int(line) == line_no
    