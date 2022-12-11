import sys

sys.setrecursionlimit(10**5)
cache= {}
def f(n):
    if n not in cache:
        if n==1: cache[n]=1
        else: cache[n]=n*n+f(n-1)
    return cache[n]
print(f(2023)-f(2019))
