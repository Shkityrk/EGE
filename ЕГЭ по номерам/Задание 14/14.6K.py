for x in range(1,10000):
    s=4**2015+2**x-2**2015+15
    count=0
    while s!=0:
        if s%2==1: count+=1
        s=s//2
    if count==500:
        print(x)
        break