from musttest.georeum.georeum import Georeum
import os


def test_select_test_case():
    path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(path, "select")
    test_path = os.path.join(root_path, "tests")
    cache_path = os.path.join(root_path, ".cache")
    georeum = Georeum(root_path, test_path)
    georeum.save()  # stocked here and results select_test_case() not working.
    assert os.path.exists(os.path.join(cache_path, "cache.pkl"))
    assert os.path.exists(os.path.join(cache_path, "coverage.bin"))
    # make change to src/adder.py
    with open(os.path.join(root_path, 'src/adder.py'), 'w+') as f:
        f.write("""def add(a: int, b: int) -> int:
    c = a + b
    if c < 100:
        c = c + 1  # This line is added
        return c
    else:
        print("Result is too large: %d" % c)
        return -1

""")
        f.close()

    georeum = Georeum(root_path, test_path)
    selected = georeum.select_test_case()
    assert os.path.join(test_path, "test_small.py") in selected
    assert not (os.path.join(test_path, "test_large.py") in selected)


def test_test_run():
    path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(path, "select")
    test_path = os.path.join(root_path, "tests")
    georeum = Georeum(root_path, test_path)
    # georeum.save()
    selected = georeum.select_test_case()
    ran = georeum.test_run()
    for test in selected:
        assert test not in ran
