from fnmatch import *
k=0
def dels(n):
    d=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:d|={i,n//i}
    return sum(d)
for n in range(10**6,10**7+1):
    if fnmatch(str(n),'9?*55*7'):
        print(n,dels(n)%21)
