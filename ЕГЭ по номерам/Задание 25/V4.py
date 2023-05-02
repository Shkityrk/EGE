def d(x):
    a=[]
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            a.append(i)
            a.append(x//i)
    return sorted(a)
kol=0

for n in range(860000,1000000):
    dels=d(n)
    if len(dels)>=2:
        m=max(dels)-min(dels)
        if m%100==18:
            print(n,m)
            kol+=1
            if kol==5:break