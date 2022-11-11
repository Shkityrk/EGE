import sys
from functools import lru_cache
sys.setrecursionlimit(100000)
@lru_cache
def isint(n):
    s=str(n)
    if s[-1]=='0' and s[-2]=='.' in s: return 1
    else: return 0
def f(n):
    if isint(n**0.5)==1: return int(n**0.5)
    else: return f(n+1)+1
print(f(4850)+f(5000))

