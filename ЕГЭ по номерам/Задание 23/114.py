from functools import lru_cache
@lru_cache(None)
def f(c,e,s):
    if c>e: return 10**10
    if c==e: return s
    if c<e: return min(f(c+1,e,s+1), f(c+2,e,s+1), f(c*2,e,s+1))
print(f(1,28,0))