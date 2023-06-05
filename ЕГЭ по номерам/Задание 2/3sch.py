import itertools


def f(x,y,z):
    return (x and (not z)) or ((not y) and (not z))
t=[(0,0,0),
   (0,0,1),
   (0,1,0),
   (0,1,1),
   (1,0,0),
   (1,0,1),
   (1,1,0),
   (1,1,1)]
for p in itertools.permutations('xyz'):
    if [f(**dict(zip(p,r))) for r in t]==[1,0,0,0,1,0,1,0]:
        print(p)
        break