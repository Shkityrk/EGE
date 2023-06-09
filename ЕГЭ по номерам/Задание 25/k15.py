def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return 0
    return 1
def primeDels(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0 and isPrime(i)==1:s.append(i)
        if n%(n//i)==0 and isPrime(n//i)==1:s.append(n//i)
    return sum(set(s))
k=0
for i in range(500000-1,1,-1):
    s=primeDels(i)
    if s!=0 and s%10==0:
        print(i,s)
        k+=1
        if k>=10:break