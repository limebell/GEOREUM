from src.cover.cover import Line, Cover
import unittest

class TestLine(unittest.TestCase):
    def test_line(self):
        filepath = "/path/to/python/test.py"
        line_no = 112
        line_text = "def foo():\n"
        line = Line(filepath, line_no, line_text)
        self.assertEqual(str(line), line_text[:-1])
        self.assertEqual(int(line), line_no)


if __name__ == '__main__':
    unittest.main()