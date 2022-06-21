for x in range(2,10000):
    s=4**1014-2**x+12
    count =0
    while s!=0:
        if s%2==0: count+=1
        s=s//2
    if count==2000:
        print(x)
        break