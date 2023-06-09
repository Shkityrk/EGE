from fnmatch import *
def dels(n):
    d=[]
    if n%2==0:d.append(n)
    for i in range(2,int(n**0.5)+1):
        if n%i==0 and i%2==0:d.append(i)
        if n % (n//i) == 0 and (n//i) % 2 == 0: d.append(n//i)
    return set(d)
k=0
for n in range(65000,10**8):
    if fnmatch(str(n),'6*97*5?'):
        d=dels(n)
        if len(d)>=4:
            print(n, sum(d))
            k+=1
            if k>=7:break