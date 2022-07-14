for a in range(1,1000):
    f=1
    for x in range(1,1000):
        f*=(x%a==0)<=((x%14==0) and (x% 21==0))
    if f==1:
        print(a)
        break