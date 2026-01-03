# string functions

def hasupper(st : str) -> bool:
    for c in st:
        if c.isupper():
            return True

    return False


def countupper(st: str) -> int:
    cnt = 0
    for c in st:
        if c.isupper():
           cnt += 1

    return cnt
