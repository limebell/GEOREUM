from src.cover.cover import Line, Cover
from src.diff.hashcash import hexdigest
import os 
import unittest


class TestCover(unittest.TestCase):
    def test_get_coverage(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fn = 'test_cover_input.py'
        with open(os.path.join(dir_path,fn),'w+') as f:
            text = """
def foo():
    print("This is Foo")
def bar():
    print("This is Bar")
"""
            f.write(text)
            f.close()
        covered = Cover.get_coverage(os.path.join(dir_path,"test_cover_input.py"),\
                                    os.path.join(dir_path,"../../")) # RootDIR as cs453
        key = hexdigest(f"{os.path.join(dir_path,fn)}2def foo():")
        self.assertEqual(str(covered[key]),text.split("\n")[1])
        self.assertEqual(int(covered[key]),2)
        os.remove(os.path.join(dir_path,fn))

if __name__ == '__main__':
    unittest.main()