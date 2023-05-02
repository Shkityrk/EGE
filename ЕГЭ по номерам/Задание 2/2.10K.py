from itertools import *

def f(x,y,z):
    return not(x==(y<=z))


for p in permutations('xyz'):
    t = [(0, 0, 1),
         (0, 1, 1)]
    if [f(**dict(zip(p,r)))for r in t]==[1,0]:
        print(p)