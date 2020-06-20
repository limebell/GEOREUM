from src.diff.manager import Manager
import os


def test_update():
    path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(path, "update")
    cache_dir = os.path.join(root_path, ".cache")
    manager = Manager(root_path)

    manager.update_cache()
    assert os.path.exists(cache_dir)
    assert os.path.exists(os.path.join(cache_dir, "cache.pkl"))


def test_analyze():
    path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(path, "analyze")
    manager = Manager(root_path)
    report = manager.analyze()

    assert 2 == len(report.modified_files())
    assert "source1" in [df.name for df in report.modified_files()]
    assert "folder\\source2" in [df.name for df in report.modified_files()]
    for df in report.diff_formats:
        if df.name == "source1":
            assert df.added == []
            assert df.removed == [2]
        elif df.name == "folder\\source2":
            assert df.added == [1]
            assert df.removed == []
