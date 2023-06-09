def f(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if i%10==7: s.append(i)
            if (n//i)%10==7: s.append(n//i)
    return sorted(set(s))
k=0
for n in range(550_001,10000000):
    r=f(n)
    if len(r)==3:
        print(n,max(r))
        k+=1
        if k>=5:break


