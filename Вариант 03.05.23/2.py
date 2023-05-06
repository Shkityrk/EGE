from itertools import *

def f(x,y,z,w):
    return ((not z) == (not y)) or ((not x) and y) or w
for a1,a2,a3,a4,a5,a6,a7 in product([0,1],repeat=7):
    t=[(a1,1,a2,1),
       (1,1,a3,a4),
       (1,a5,a6,a7)]
    for p in permutations('xyzw'):
        if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
            print(p)
