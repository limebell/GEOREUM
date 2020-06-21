from musttest.cover.cover import Line


def test_line():
    filepath = "/path/to/python/test.py"
    line_no = 112
    line_text = "def foo():\n"
    line = Line(filepath, line_no, line_text)
    line.getHash()
    assert str(line) == line_text[:-1]
    assert int(line) == line_no
    
    if str(line) == line_text[:-1]:
        print("If branch. This should be printed")
    else:
        print("Else branch. This should not be printed")
