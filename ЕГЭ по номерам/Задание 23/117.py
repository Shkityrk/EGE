ch=set()
from functools import*
@lru_cache(None)
def f(c,s):
    if s==7: ch.add(c)
    else:return f(c+1,s+1), f(c+5,s+1), f(c*3,s+1)
f(1,0)
print(len(ch))
