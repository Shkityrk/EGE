import itertools


def f(x,y,z,w):
    return (x<=y) and (not(z)<=x) or w

t=[(0,0,0,1),
   (0,0,1,0),
   (0,1,0,1)]

for p in itertools.permutations('xyzw'):
    if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
        print(p)
        break