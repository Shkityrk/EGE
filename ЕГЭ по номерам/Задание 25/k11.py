def f(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    return sorted(set(s))
k=0
for n in range(300_000,10000000):
    r=[x for x in f(n) if x%3==0]
    if len(r)==5:
        print(n,max(r))
        k+=1
        if k>=5:break


