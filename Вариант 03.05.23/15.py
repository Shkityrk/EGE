def f(x,y,a):
    return ((2*x+y)!=150) or (not(50<=x<=70)) or (a>y)

for a in range(1,100):
    if all(f(x,y,a) for x in range(1,10000) for y in range(1,10000)):
        print(a)
        break