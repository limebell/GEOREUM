from src.georeum.georeum import Georeum
import os


def test_search_by_file():
    path = os.path.dirname(os.path.abspath(__file__))
    files = Georeum.search_py_file(os.path.join(path, "update"))
    path = os.path.join(path, "update")
    assert 4 == len(files)
    assert os.path.join(path, "__init__.py") in files
    assert os.path.join(path, "update.py") in files
    assert not (os.path.join(path, "update.py_after") in files)
    assert not (os.path.join(path, "update.py_before") in files)
    assert os.path.join(path, "folder" + os.path.sep + "__init__.py") in files
    assert os.path.join(path, "folder" + os.path.sep + "sample.py") in files


def test_save():
    path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(path, "save")
    test_path = os.path.join(root_path, "tests")
    georeum = Georeum(root_path, test_path)
    georeum.save()
