f=open('27-144a.txt')
n=int(f.readline())
k=int(f.readline())

a=[int(x) for x in f.readlines()]

k25=[0]*25
count=0
for i in range(k,n):
    ost=a[i-k]%25
    k25[ost]+=1

    ost2=0 if a[i]%25==0 else 25-a[i]%25
    count+=k25[ost2]
print(count)