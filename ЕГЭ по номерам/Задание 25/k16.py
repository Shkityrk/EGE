def isPrime(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
def dels(n):
    d=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:d|={i,n//i}
    return sorted(d)
for n in range(125697,125721+1):
    d=[i for i in dels(n) if isPrime(i)]
    if len(d)==2 and d[0]*d[1]==n:
        print(d[0], d[1])