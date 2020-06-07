import src.diff.hashcash as hashcash
import pytest
import os


def test_hexdigest():
    input_str = "hello world"
    expected = "256c83b297114d201b30179f3f0ef0cace9783622da5974326b436178aeef610"
    actual = hashcash.hexdigest(input_str)
    assert actual == expected


def test_hexdigest_empty():
    with pytest.raises(hashcash.HashError) as excinfo:
        hashcash.hexdigest('')

    assert "Input should be a non-empty string." in str(excinfo.value)


def test_hexdigest_non_string():
    with pytest.raises(hashcash.HashError) as excinfo:
        hashcash.hexdigest(3)

    assert "Input should be a non-empty string." in str(excinfo.value)


def test_hashcash():
    path = os.path.dirname(os.path.abspath(__file__))
    f = open(os.path.join(path, "input.txt"), 'r')
    lines = f.readlines()
    assert len(lines) == 9
    hashes = hashcash.hashcash(lines)
    assert len(hashes) == 10
    assert hashes[0] == "f74c4de79917668ed5f3a529882535f0d101236608e6493e9358f297ae02b0ae"

    index = 0
    for hash_value in hashes[1:]:
        assert hash_value == hashcash.hexdigest(lines[index])
        index += 1
