import itertools
def f(x,y,z):
    return (x or z)<=(x==y)
for a1,a2,a3 in itertools.product([0,1],repeat=3):
    t=[(a1,0,a2),
       (a3,0,0)]
    if len(t)==len(set(t)):
        for p in itertools.permutations('xyz'):
            if [f(**dict(zip(p,r))) for r in t]==[0,0]:
                print(p)
                break