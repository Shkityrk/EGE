from itertools import *
l=set()
def f(x,y,z,w):
    return (x==y)<=(z==w)
t=[(0,0,0,1),
   (1,1,1,0)]
for p in permutations('xyzw'):
    if [f(**dict(zip(p,r))) for r in t]==[0,0]:
        s=''.join(p)
        l.add(s)
print((l))
