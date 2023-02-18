from functools import *
cache={}
@lru_cache(None)
def f(n):
    if n not in cache:
        if n==1:cache[1]=1
        if n>1: cache[n]=(3*n+5)*cache[n-1]
    return cache[n]
print(f(2073)/f(2070))