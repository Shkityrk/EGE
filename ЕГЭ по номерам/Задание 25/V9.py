def dels(x):
    a=[]
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            a.append(i)
            a.append(x//i)
    return sorted(a)
kol=0
for n in range(850001,1_000_000):
    d=dels(n)
    if len(d)>=2:
        f=max(d)-min(d)
        if f%7==0:
            print(n,f)
            kol+=1
            if kol>8:break