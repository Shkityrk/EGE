from itertools import *

def f(x,y,z,w):
    return (y<=x or z) and (z<=y)
t=[(1,0,0,0),
   (1,1,0,0),
   (1,1,0,1),
   (0,1,1,0)]
for p in permutations('xyzw'):
    if [f(**dict(zip(p,r)))for r in t]==[0,0,0,0]:
        print(p)