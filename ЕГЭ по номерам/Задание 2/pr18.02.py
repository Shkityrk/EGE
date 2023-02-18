from itertools import *
def f(x,y,z,w):
    return ((w<=z) and ((not x)<=y))<=(y==w) or (z and (not x))
for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
    t=[(0,0,0,a1), (1,1,a2,1), (0,a3,a4,a5)]
    if len(t)==len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
                print(p)