for x in range(1,100000):
    n=4**1014-2**x+12
    k=0
    while n!=0:
        if n%2==0:k+=1
        n=n//2
    if k==2000:
        print(x)
        break