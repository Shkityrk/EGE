from functools import *
c=0
@lru_cache(None)
def f(c,e):
    if c>e:return 0
    if c==e:return 1
    if c<e:return f(c+1,e)+f(c*2,e)+f(c*3,e)
for i in range(2,10000,2):
    if f(i,15):c+=1
print(c)