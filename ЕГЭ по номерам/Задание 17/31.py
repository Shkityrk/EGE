def f(n,x):
    s=''
    while n!=0:
        s+=str(n%x)
        n//=x
    return s[::-1]
k=0
mn=100000
for n in range(1000, 10000):
    if len(f(n,5))>=6 and (f(n,5)[-2:]=='21' or f(n,5)[-2:]=='23'):
        k+=1
        mn= min(mn,n)
print(k,mn)
