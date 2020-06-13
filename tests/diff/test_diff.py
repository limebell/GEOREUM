from src.diff.diff import Diff, DiffFormat, DiffReport, DiffError
from src.diff.hashcash import hashcash


def test_diff_format():
    df1 = DiffFormat("name")
    assert df1.modified() is False

    df2 = DiffFormat("name")
    df2.added.append(1)
    assert df2.modified() is True

    df3 = DiffFormat("name")
    df3.removed.append(3)
    assert df3.modified() is True

    df4 = DiffFormat("name")
    df4.added.append(2)
    df4.removed.append(4)
    assert df4.modified() is True


def test_diff_analyze():
    # Test case is modified from differ-example
    # https://docs.python.org/2.4/lib/differ-examples.html
    text1 = '''1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complicated is better than complex.
'''.splitlines(1)
    text2 = '''1. Beautiful is better than ugly.
3. Simple is better than complex.
4. Complicated is better than complex.
5. Flat is better than nested.
'''.splitlines(1)
    cached = hashcash(text1)
    hashed = hashcash(text2)
    df = DiffFormat("temp")
    Diff.analyze(df, hashed, cached)

    assert df.modified() is True
    assert df.added == [4]
    print(df.added)
    assert df.removed == [2]
