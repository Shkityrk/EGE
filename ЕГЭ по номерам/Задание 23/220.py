from functools import *
@lru_cache(None)
def f(c,e):
    if c<e: return 0
    if c==e: return 1
    if c>e: return f(c-3,e)+f(c//7,e)
print(f(50,1))

