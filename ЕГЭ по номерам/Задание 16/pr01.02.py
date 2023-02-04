from functools import lru_cache

from sys import setrecursionlimit
setrecursionlimit(3000)
cache={}
@lru_cache(None)

def f(n):
    if n not in cache:
        if n==1: cache[n]=1
        else: cache[n]=n*f(n-1)
    return cache[n]
for i in range(1,1000):
    f(i)
for i in range(1000,2000):
    f(i)
for i in range(2000,2024):
    print(f(i))

print((f(2023)-f(2022))/f(2020))