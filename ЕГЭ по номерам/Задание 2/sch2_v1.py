import itertools


def f(x,y,z,w):
    return not(x<=y) and (w<=z)

t=[(1,0,0,1),
   (0,0,0,1),
   (1,0,1,1)]
if len(t)==len(set(t)):
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
            print(p)
            break