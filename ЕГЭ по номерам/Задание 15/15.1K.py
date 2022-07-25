for a in range(1,1000):
    f=1
    for x in range(1,1000):
        f*=((x%a==0) and (x%24==0) and (x%16!=0))<= (x%a!=0)
    if f== 1:
        print(a)
        break