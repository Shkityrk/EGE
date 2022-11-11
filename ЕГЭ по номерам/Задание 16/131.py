cache={}
from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n==1: return 1
    else: return n*f(n-1)
print(f(2023),f(2020))