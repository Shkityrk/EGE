import itertools


def f(x,y,z,w):
    return not (y) and x and (w<=z)

t=[(1,0,0,0),
   (1,0,1,0),
   (1,0,1,1)]
if len(t)==len(set(t)):
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p,r))) for r in t]==[1,1,1]:
            print(p)
            break