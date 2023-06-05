import itertools


def f(x,y,z,w):
    return not(w) and ((not y) and x or (not z) and y and (not x))
t=[(0,0,0,1),
   (1,0,0,0),
   (1,1,0,0)]
for p in itertools.permutations('xyzw'):
    if [f(**dict(zip(p,r))) for r in t]==[1,1,1]:
        print(p)
        break