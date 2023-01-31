from itertools import *
def f(a,b,c,d):
    return (a<=b) and (c<=d) or (not c)
t=[(1,0,1,0), (0,0,1,1), (0,1,1,1), (1,0,1,1)]

for p in permutations('abcd'):
    if [f(**dict(zip(p,r))) for r in t]==[0,0,0,0]:
        print(p)