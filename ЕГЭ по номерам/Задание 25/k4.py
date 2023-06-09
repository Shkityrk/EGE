def d(n):
    s=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s+=i
            s+=n//i
    return s
k=0
for n in range(150000,4_000_000):
    r=d(n)
    if r%13==10 and r!=0:
        print(n,r)
        k+=1
        if k>7:break
