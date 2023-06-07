import itertools
def f(x,y,z,w):
    return ((w or x)<=(w and (not z))) and (not y)
for a1,a2,a3,a4,a5,a6,a7,a8 in itertools.product([0,1],repeat=8):
    t=[(a1,a2,a3,1),
       (a4,a5,1,a6),
       (a7,1,1,a8)]
    if len(t)==len(set(t)):
        for p in itertools.permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t]==[1,1,1]:
                print(p)
                break