import hashlib

DIGEST_SIZE = 32


class HashError(BaseException):
    def __init__(self, msg: str):
        super().__init__(msg)


def hexdigest(target: str):
    """
    Returns hexdigest of a string using blake2b.
    :param target: Target string to hash of 'utf-8'.
    :return: Hexdigest value of a string.
    """
    if not target:
        return ""
    if not isinstance(target, str):
        raise HashError("Input should be a string but %s" % repr(target))

    blake = hashlib.blake2b(target.encode("utf-8"), digest_size=DIGEST_SIZE)
    return blake.hexdigest()


def hashcash(lines: list) -> list:
    """
    Returns hash of the file using blake2b. The first line of the output is
    hash value of the file, and next lines are hash value of each line.
    :param lines: Lines of the file to hash in string.
    :return: Hashed value in list.
    """
    hashes = []
    # hash each line
    for line in lines:
        hashes.append(hexdigest(line))

    # hash all hashes altogether
    total_hash = hexdigest(''.join(hashes))
    hashes.insert(0, total_hash)

    return hashes
