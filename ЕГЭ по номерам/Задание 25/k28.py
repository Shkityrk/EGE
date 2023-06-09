from fnmatch import *
k=0
def dels(n):
    d=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:d|={i,n//i}
    return sum(d)
for n in range(1,10**7):
    if fnmatch(str(n),'?6*6*?6'):
        if n%6==0 and n%7==0 and n%8==0:
            d=dels(n)
            print(n,d)
            k+=1
            if k>=7:break
