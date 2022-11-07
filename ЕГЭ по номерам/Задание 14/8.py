for x in range(1,1000):
    k=0
    n=36**17-6**x+71
    while n!=0:
        k+=n%6
        n//=6
    if k==61:
        print(x)
        break