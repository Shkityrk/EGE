from itertools import *

def f1(x,y,z,w):
    return ( x or (not y))<=(w==z)
def f2(x,y,z,w):
    return (x or (not y))==(z<=w)

for a1,a2,a3,a4 in product([0,1],repeat=4):
    t=[(0,a1,0,0),
       (a2,1,1,a3),
       (a4,0,0,0)]
    if len(t)==len(set(t)):
        for p in permutations('xywz'):
            if [f1(**dict(zip(p,r))) for r in t][0]==0 and [f2(**dict(zip(p,r))) for r in t][0]==0:
                print(p)
                break
