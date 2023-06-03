from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n>100000:return n
    if n<=100000: return f(n+1)+5*n+2
print(f(3)-f(7))