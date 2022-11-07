from functools import *
import sys
sys.setrecursionlimit(100000)

@lru_cache(None)
def f(n):
    if n<3: return n+1
    if n>=3 and n%2==0: return f(n-2)+n-2
    if n >= 3 and n % 2 != 0: return f(n + 2) + n + 2
k=0
for n in range(1,10000):
    if len(str(f(n)))==5: k+=1
print(k)