import itertools


def f(x,y,z,w):
    return w and (z==(y and (not x)))
for a1,a2,a3,a4,a5,a6,a7,a8,a9,a10 in itertools.product([0,1],repeat=10):
    t=[(a1,0,a2,a3),
       (a4,a5,a6,0),
       (0,0,a7,a8),
       (0,0,a9,a10)]
    if len(t)==len(set(t)):
        for p in itertools.permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t]==[1,1,1,1]:
                print(p)
                break
