for x in range(1,100000):
    n=4**2015+2**x-2**2015+15
    k=0
    while n!=0:
        if n%2==1:k+=1
        n//=2
    if k==500:
        print(x)
        break