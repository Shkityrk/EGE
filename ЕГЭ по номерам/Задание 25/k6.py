def f(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    return sum(s)//len(s) if len(s)!=0 else 0
k=0
for n in range(550000,3_000_000):
    if f(n)%31==13:
        print(n,f(n))
        k+=1
        if k>=5:
            break