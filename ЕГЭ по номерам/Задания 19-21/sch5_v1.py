from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 3, b), (a, b * 3)


@lru_cache(None)
def f(h):
    if (sum(h) >= 100):
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if any(f(x) == 'P1' for x in moves(h)):
        return 'V1'


for s in range(1, 92):
    h = 7, s
    if f(h) == 'V1':
        print(s)
        break