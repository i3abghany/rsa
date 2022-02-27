
def to_numeric(message: str):
    res = 0
    base = 1
    for c in message:
        res += ord(c) * base
        base *= 256
    return res


def to_string(message: int):
    res = str()
    while message > 0:
        c = chr(message % 256)
        res += c
        message = message // 256

    return res

