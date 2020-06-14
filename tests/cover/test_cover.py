from src.cover.cover import Cover
from src.diff.hashcash import hexdigest
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
    not_covered_line_no = 31
    not_covered_text = "    hashes = []"
    not_covered_key = hexdigest(
        f"{file_path}{not_covered_line_no}{not_covered_text}")

    assert str(covered[covered_key]) == text
    assert int(covered[covered_key]) == line_no
    with pytest.raises(TypeError):
        covered[not_covered_key]


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
    not_covered_line_no = 31
    not_covered_text = "    hashes = []"
    not_covered_key = hexdigest(
        f"{file_path}{not_covered_line_no}{not_covered_text}")

    assert str(covered[covered_key]) == text
    assert int(covered[covered_key]) == line_no
    with pytest.raises(TypeError):
        covered[not_covered_key]
    # assert 3 == 4
