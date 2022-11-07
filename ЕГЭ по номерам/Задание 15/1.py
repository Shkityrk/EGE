for a in range(1,1000):
    f=1
    for x in range(1,10000):
        f*=(((x%13==0)<=(x%21!=0)) or (x+a>=500))
    if f==1:
        print(a)
        break