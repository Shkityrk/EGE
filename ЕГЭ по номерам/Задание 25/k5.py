def d(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    return sorted(set(s))
k=0
for n in range(250200,4_000_000):
    r=d(n)
    if len(r)>=2 and (r[0]+r[-1])%123==17:
        print(n,r[0]+r[-1])
        k+=1
        if k>5:
            break