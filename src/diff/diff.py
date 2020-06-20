class DiffFormat:
    def __init__(self, name: str):
        self.name = name
        self.added = []
        self.removed = []

    def __repr__(self):
        return "file: %s / added: %s / removed: %s" % \
               (self.name,
                ", ".join([str(i) for i in self.added]),
                ", ".join([str(i) for i in self.removed]))

    def modified(self) -> bool:
        return (not self.added and not self.removed) is False


class DiffReport:
    def __init__(self, diff_formats):
        self.diff_formats = diff_formats

    def __repr__(self):
        return "diff report\n%s" % \
               '\n'.join([repr(df) for df in self.diff_formats])

    def modified_files(self) -> list:
        return [df for df in self.diff_formats if df.modified()]


class DiffError(BaseException):
    def __init__(self, msg: str):
        super().__init__(msg)


class Diff:
    @staticmethod
    def __find_first(target: str, elements: list, start: int = 0, end: int = -1) -> int:
        index = start
        for elem in elements[start:end]:
            if target == elem:
                return index

            index += 1

        return -1

    @staticmethod
    def analyze(df: DiffFormat, hashed: list, cached: list) -> DiffFormat:
        hashed_index = 1
        cached_index = 1
        for cached_index in range(1, len(cached)):
            if hashed_index >= len(hashed):
                df.removed = df.removed + list(range(cached_index, len(cached)))
                break
            cached_hash = cached[cached_index]
            if cached_hash == hashed[hashed_index]:
                # line is not added nor removed
                hashed_index += 1
            else:
                # if not exist in further cached, it is added
                # else if exist in further cached, element between them are removed
                # todo: what if same line is added not removed?
                first = Diff.__find_first(cached_hash, hashed, hashed_index, -1)
                if first == -1:
                    # was cached, but not exist
                    df.removed.append(cached_index)
                else:
                    # new lines were added between hashed_index ~ first
                    df.added = df.added + ([cached_index] * (first - hashed_index))
                    hashed_index = first + 1

        # new lines added at the end
        # print("number of new lines added at the end: %d" % (len(hashed) - hashed_index))
        df.added = df.added + ([cached_index] * (len(hashed) - hashed_index))
        return df
