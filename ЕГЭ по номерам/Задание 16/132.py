cache={}
from sys import setrecursionlimit
setrecursionlimit(10000)
 
def f(n):
    if n not in cache:
        if n==1: cache[1]= 1
        else: cache[n]= (2*n-1)*f(n-1)
    return cache[n]
print(f(3516)//f(3513))

