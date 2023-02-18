for a in range(100,1,-1):
    f=1
    for x in range(1,1000):
        for y in range(1, 1000):
            if ((x+y<=22) or (y<=x-6) or (y>=a))==0:
                f=0
                break
    if f==1:print(a)