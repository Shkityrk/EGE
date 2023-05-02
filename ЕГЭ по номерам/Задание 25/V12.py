def dels(x):
    a=[]

    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            a.append(i)
            a.append(x//i)
    return sorted(a)
k=0
for n in range(850001,1_000_000):
    if len(dels(n))>=2:
        f=max(dels(n))-min(dels(n))
        if f%11==0:
            print(n,f)
            k+=1
            if k>=6:break