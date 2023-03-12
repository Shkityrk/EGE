def f(x,y,a):
    return ((x+y<=32) or (y<=x+4) or (y>=a))

for a in range(1,100):
    fl=1
    for x in range(1,1000):
        for y in range(1,1000):
            if f(x,y,a)==0:
                fl=0
                break
    if fl==1:print(a)