from itertools import *
def f(x,y,z,w):
    return ((y<=x) or ((not z) and w))==(w==x)

for a1,a2,a3 in product([0,1],repeat=3):
    t=[(a1,1,0,0),
       (0,0,0,1),
       (0,1,a2,a3)]
    if len(t)==len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t]==[1,1,1]:
                print(p)
