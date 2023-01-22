from itertools import *

def f(x,y,z):
    return (x<=y) and (y<=z)

table = [(1,0,0), (1,0,1)]
for p in permutations('xyz'):
    if [f(**dict(zip(p,row))) for row in table]==[0,1]:
        print(p)
        