def f(x,a):
    return ((x%15==0) and (x%21!=0)) <= ((x%a!=0) or (x%15!=0))
for a in range(1,1000):
    if all(f(x,a) for x in range(1,10000)):
        print(a)
        break