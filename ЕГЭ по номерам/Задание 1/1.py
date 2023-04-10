from itertools import *

g = 'АЖЗЕБАДГВЕЖД'
t = '''
.*...**.
*..**.*.
....*..*
.*..*...
.***.*..
*...*...
**.....*
..*...*.
'''.split()

print(all(t[i][j] == t[j][i] for i in range(8) for j in range(8)))  # проверка на правильность заполнения таблицы


def f(x, y):
    x, y = p.index(x), p.index(y)
    return t[x][y] == '*'


for p in permutations(set(g)):
    if all(f(x, y) == (x + y in g or y + x in g) for x, y in product(p, p)):
        print(*p, sep='')
