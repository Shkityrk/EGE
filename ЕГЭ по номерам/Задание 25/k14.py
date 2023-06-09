def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return 0
    return 1
def primeDels(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0 and isPrime(i)==1:s.append(i)
        if n%(n//i)==0 and isPrime(n//i)==1:s.append(n//i)
    return sorted(set(s))
for i in range(25317,51237+1):
    s=primeDels(i)
    if len(s)>=6:
        print(i, max(s))