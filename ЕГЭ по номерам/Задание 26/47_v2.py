from bisect import *
f=open('data/26-47.txt')
n=int(f.readline())

a=[int(x) for x in f.readlines()]
a.sort()
ans=[]
for i in range(n):
    for j in range(i+1,n):
        sr=(a[i]+a[j])//2
        count=bisect_left(a,sr)
        if count%100==0:ans.append(count)
print(len(ans), max(ans))