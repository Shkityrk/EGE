import itertools


def f(x,y,z,w):
    return (x==(not y)) <=(z==(y or w))
for a1,a2,a3,a4,a5 in itertools.product([0,1],repeat=5):
    t=[(0,a1,0,a2),
       (0,0,a3,0),
       (0,a4,a5,0)]
    if len(t)==len(set(t)):
        for p in itertools.permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
                print(p)
                break