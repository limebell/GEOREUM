from musttest.cover.cover import Cover
from musttest.diff.hashcash import hexdigest
import os
import pytest



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
