from itertools import *

def f(a,b,c,d):
    return  (a<=d) and (not(b<=c))
t=[(1,0,1,0), (1,1,1,0),(0,0,1,0)]
for p in permutations('abcd'):
    if [f(**dict(zip(p,r))) for r in t]==[1,1,1]:
        print(p)