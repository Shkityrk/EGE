def d(x):
    a=[]
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            a.append(i)
            a.append(x//i)
    return sorted(a)
kol=0
for n in range(800000,1,-1):
    de=d(n)
    if len(de)>=2:
        m=max(de)-min(de)
        if m%23==0:
            print(n,m)
            kol+=1
            if kol==5:break