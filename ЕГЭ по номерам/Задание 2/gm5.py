from itertools import *

def f(x,y,z,w):
    return ((y or x)==((y<=w) or (not z)))

t=[(1,0,0,0), (0,1,0,0), (1,0,1,0)]
for p in permutations('xyzw'):
    if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
        print(p)