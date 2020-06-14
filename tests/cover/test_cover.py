from src.cover.cover import Cover
from src.diff.hashcash import hexdigest
import os 

    
def test_get_coverage_pytest():
    fn = 'test_line.py'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    covered = Cover.get_coverage(args = ['pytest', os.path.join(dir_path, fn)],
                                root_path = os.path.join(dir_path,"../../"),
                                module_use = True)

    file_path = os.path.abspath(os.path.join(dir_path, '../../src/diff/hashcash.py'))
    line_no = 1
    text = "import hashlib"
    key = hexdigest(f"{file_path}{line_no}{text}")

    assert str(covered[key]) == "import hashlib"
    assert int(covered[key]) == 1


def test_get_coverage_unittest():
    fn = 'tests.cover.test_unittest_line.TestLine'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    covered = Cover.get_coverage(args = ['unittest', fn],
                                root_path = os.path.join(dir_path,"../../"),
                                module_use = True)
    file_path = os.path.abspath(os.path.join(dir_path, '../../src/diff/hashcash.py'))
    line_no = 1
    text = "import hashlib"
    key = hexdigest(f"{file_path}{line_no}{text}")

    assert str(covered[key]) == "import hashlib"
    assert int(covered[key]) == 1
    # assert 3 == 4