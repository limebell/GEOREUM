from src.diff.diff import Diff, DiffFormat, DiffReport, DiffError
import src.diff.hashcash as hashcash
import os


class Manager:
    def __init__(self, dir_path: str, rel_cache_path: str):
        """
        An instance of diff management module.
        :param dir_path: Absolute path of target path to analyze.
        :param rel_cache_path: Relative path of cache files. (default = ./.cache)
        """
        self.dir_path = dir_path
        self.cache_path = os.path.join(dir_path, rel_cache_path)

    def __analyze_file(self, file_path: str) -> DiffFormat:
        # todo: remove empty newlines
        # todo: remove comments
        rel_path = os.path.relpath(file_path, self.dir_path)
        f = open(file_path, 'r')
        lines = f.readlines()
        hashed = hashcash.hashcash(lines)
        if not os.path.isdir(self.cache_path):
            raise DiffError("Cache directory does not exists: %s" % self.cache_path)
        cache = next((x for x in os.walk(self.cache_path) if x[2] == "rel_path"), None)
        df = DiffFormat(rel_path)
        if cache is None:
            # cache does not exists, all lines are added lines
            df.added = list(range(1, len(lines) + 1))
        else:
            # cache exists
            cache = open(os.path.join(cache[0], cache[2]))
            cached = cache.readlines()
            Diff.analyze(df, hashed, cached)

        return df

    def analyze(self) -> DiffReport:
        """
        Diff analyzer between cache and current.
        How it works:
        1. 우선 모든 파일의 복사본을 준비한다.
        2. 각 라인을 해시하여 정보를 array 등에 담는다.
        3. 전체 라인을 해시하여 파일의 정보를 대표한다.
        4. 기존에 있던 복사본의 각 파일과 해시값을 비교하여 파일 단위에 변화가 있는지 알아낸다.
        5. 변화가 있는 파일에 대해 라인 단위로 변화가 있는지 알아낸다.
        :return: A src.diff.diff.DiffReport instance.
        """
        if not os.path.isdir(self.dir_path):
            raise DiffError("Project path is empty: %s" % self.dir_path)

        if not os.path.isdir(self.cache_path):
            os.mkdir(self.cache_path)

        return DiffReport()
