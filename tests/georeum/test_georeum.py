from src.georeum.georeum import Georeum
import os


def test_search_by_file():
    path = os.path.dirname(os.path.abspath(__file__))
    files = Georeum.search_py_file(os.path.join(path, "source"))
    path = os.path.join(path, "source")
    assert 4 == len(files)
    assert os.path.join(path, "__init__.py") in files
    assert os.path.join(path, "source.py") in files
    assert not (os.path.join(path, "source.py_after") in files)
    assert not (os.path.join(path, "source.py_before") in files)
    assert os.path.join(path, "folder" + os.path.sep + "__init__.py") in files
    assert os.path.join(path, "folder" + os.path.sep + "sample.py") in files


def test_save():
    path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(path, "save")
    test_path = os.path.join(root_path, "tests")
    cache_path = os.path.join(root_path, ".cache")
    georeum = Georeum(root_path, test_path)
    georeum.save()
    assert os.path.exists(os.path.join(cache_path, "cache.pkl"))
    assert os.path.exists(os.path.join(cache_path, "coverage.bin"))


def test_select_test_case():
    path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(path, "select")
    test_path = os.path.join(root_path, "tests")
    cache_path = os.path.join(root_path, ".cache")
    georeum = Georeum(root_path, test_path)
    assert os.path.exists(os.path.join(cache_path, "cache.pkl"))
    assert os.path.exists(os.path.join(cache_path, "coverage.bin"))
    assert os.path.join(test_path, "test_small.py") in georeum.select_test_case()
    assert not (os.path.join(test_path, "test_large.py") in georeum.select_test_case())
