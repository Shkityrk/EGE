from fnmatch import *
k=0
def dels(n):
    d=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:d|={i,n//i}
    return d
for n in range(0,10**7,217):
    if fnmatch(str(n),'14?4*'):
        d=[int(x) for x in dels(n) if x%2!=0]
        print(n,sum(d))
