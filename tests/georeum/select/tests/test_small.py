from src.adder import add


def test_small():
    c = add(3, 4)
    assert c == 7
