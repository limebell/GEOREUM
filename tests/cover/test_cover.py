from src.cover.cover import Cover, get_indent, get_functions
from src.diff.hashcash import hexdigest
import os
import pytest

# def test_true():
#     assert 1 == 1

def test_get_coverage_pytest():
    fn = 'test_line.py'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    covered = Cover.get_coverage(args=['pytest', os.path.join(dir_path, fn)],
                                 root_path=os.path.join(dir_path, "../../"),
                                 module_use=True)

    file_path = os.path.abspath(os.path.join(
        dir_path, '../../src/diff/hashcash.py'))
    line_no = 20
    text = '    blake = hashlib.blake2b(target.encode("utf-8"), digest_size=DIGEST_SIZE)'
    covered_key = hexdigest(f"{file_path}{line_no}{text}")
    assert str(covered[covered_key]) == text
    assert int(covered[covered_key]) == line_no


def test_get_coverage_unittest():
    fn = 'tests.cover.test_unittest_line.TestLine'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    covered = Cover.get_coverage(args=['unittest', fn],
                                 root_path=os.path.join(dir_path, "../../"),
                                 module_use=True)

    file_path = os.path.abspath(os.path.join(
        dir_path, '../../src/diff/hashcash.py'))
    line_no = 20
    text = '    blake = hashlib.blake2b(target.encode("utf-8"), digest_size=DIGEST_SIZE)'
    covered_key = hexdigest(f"{file_path}{line_no}{text}")
    assert str(covered[covered_key]) == text
    assert int(covered[covered_key]) == line_no
    # assert 3 == 4


def test_covered_or_not():
    fn = 'test_line.py'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    covered = Cover.get_coverage(args=['pytest', os.path.join(dir_path, fn)],
                                 root_path=os.path.join(dir_path, "../../"),
                                 module_use=True)

    file_path = os.path.abspath(os.path.join(dir_path, fn))
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line_no, text in enumerate(lines):
            line_no += 1
            if "If branch" in text:  # covered case
                covered_key = hexdigest(f"{file_path}{line_no}{text[:-1]}")
                assert "If branch" in str(covered[covered_key])
            elif "Else branch" in text:  # uncovered case
                uncovered_key = hexdigest(f"{file_path}{line_no}{text[:-1]}")
                with pytest.raises(TypeError):
                    covered[uncovered_key]
        f.close()

def test_get_functions():
    assert get_indent("\td") == 1, "get indent with tab failed"
    assert get_indent("    d") == 1, "get indent with space failed,"

    fn = 'test_line.py'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fn_path = os.path.join(dir_path, fn)

    assert get_functions(fn_path)[0].name=="test_line", "get functions failed"