for a in range(1,100):
    f=1
    for x in range(1,100):
        f*=((x%a==0) and (x%36!=0))<=(x%12!=0)
    if f==1:
        print(a)
        break