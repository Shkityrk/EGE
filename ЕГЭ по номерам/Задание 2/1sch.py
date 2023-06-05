import itertools


def f(x,y,z,w):
    return not(w) and (not(z==y)) and (x or y)
for a1,a2,a3,a4 in itertools.product([0,1], repeat=4):
    t=[(1,a1,1,a2),
       (0,1,a3,0),
       (a4,1,1,0)]
    if len(t)==len(set(t)):
        for p in itertools.permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t]==[1,1,1]:
                print(p)
                break