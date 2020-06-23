from musttest.georeum.georeum import Georeum


def test_save_coverage():
    """
    save coverage of tests/georeum/pytest/test00.py
    """
    Georeum.save_coverage("tests/georeum/pytest/test00.py")


test_save_coverage()


def test_select_test_case():
    Georeum.select_test_case()
# test_select_test_case()
