from tests.georeum.select.src.adder import add


def test_large():
    c = add(300, 400)
    assert c == -1
