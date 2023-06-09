def f(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    return sorted(set(s))
k=0
for n in range(400_000_001,600_000_000):
    r = f(n)
    if len(r)>=5:
        pr=r[0]*r[1]*r[2]*r[3]*r[4]
        if pr%100==17 and pr<=n:
            print(pr,r[4])
            k+=1
            if k>=5:break