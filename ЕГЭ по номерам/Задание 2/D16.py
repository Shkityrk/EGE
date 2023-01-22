from itertools import *

def f(x,y,z,w):
     return (not(z and (not w)) or ((z<=w)==(x<=y)))
for a1,a2,a3,a4,a5,a6 in product([0,1],repeat=6):
    t=[(1,a1,a2,a3), (1,1,a4,1), (1,a5,a6,1)]
    if len(t)==len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
                print(p)