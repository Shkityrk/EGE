from functools import *
def m(h):
    a=[]
    if h%2==0:a.append(h//2)
    else: a.append(h-2)
    if h%3==0: a.append(h//3)
    else: a.append(h-3)
    return a
@lru_cache(None)
def g(h):
    if h==1: return 'w'
    if any(g(i)=='w' for i in m(h)): return 'p1'
    if all(g(i) == 'p1' for i in m(h)): return 'v1'
    if any(g(i)=='v1' for i in m(h)): return 'p2'
    if all(g(i) == 'p1' or  g(i) == 'p2' for i in m(h)): return 'v2'
for i in range(2,37):
    print(i,g(i))