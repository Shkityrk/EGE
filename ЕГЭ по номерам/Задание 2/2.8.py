from itertools import *

def f(x,y,z,w):
    return (not y) and x and ((not z) or w)

for p in permutations('xyzw'):
    t=[(0,1,0,0),
       (1,1,0,0),
       (1,1,1,0)]
    if [f(**dict(zip(p,r))) for r in t]==[1,1,1]:print(p)