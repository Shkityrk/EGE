from functools import *

def m(h):
    a,b=h
    return (a+1,b),(a*3,b),(a,b+1),(a,b*3)
@lru_cache(None)
def g(h):
    a,b=h
    if a+b>=88: return 'w'
    if any(g(i)=='w' for i in m(h)): return 'p1'
    if all(g(i) == 'p1' for i in m(h)): return 'v1'
    if any(g(i)=='v1' for i in m(h)): return 'p2'
    if all(g(i) == 'p1' or g(i) == 'p2'  for i in m(h)): return 'v2'

for i in range(1,81):
    h=6,i
    if g(h)=='p1':print(i,g(h))