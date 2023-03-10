from fnmatch import *
def d(n):
    a=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            a.append(i)
            a.append(n//i)
    return sum(a)

k=0
for x in range(10**7,1,-1):
    if fnmatch(str(x),'9?*55*7'):
        print(x, d(x)% 21)
        k+=1
        if k>6:break