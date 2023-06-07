def f(x,y,a):
    return (2*x+3*y<a) or (x>y) or (y>24)
for a in range(1,1000):
    if all(f(x,y,a) for x in range(1,10000) for y in range(1,10000)):
        print(a)
        break