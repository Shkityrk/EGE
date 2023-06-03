from math import *
f=open('27-36b.txt')
n=int(f.readline())
s=0
list=[]
for i in range(n):
    a=[int(x) for x in f.readline().split()]
    a=[gcd(a[0],a[1]),gcd(a[0],a[2]),gcd(a[1],a[2])]
    a=sorted(a, reverse=True)
    s+=max(a)
    list.append(a[0]-a[1])

if s%10==0:print(s)
else:
    list=sorted(list)
    for i in range(len(list)):
        if (s-list[i])%10==0:
            print(s-list[i])
            break
