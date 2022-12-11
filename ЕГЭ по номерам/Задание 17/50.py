def f(n,x):
    s=[]
    for k in range(1,int(n**0.5)+1):
        if k%x==0:
            s.append(k)
            s.append(n//k)
    return sorted(s)
k=0
mn=10**10
for n in range(331,8752):
    if len(f(n,10))==len(f(n,16)) and n%5==0 and n%25!=0:
        k+=1
        mn=min(mn,n)
print(k,mn)