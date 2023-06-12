f=open('schelchok/7_B__1vjy4.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
ans=-10**20
mchet=m=-10**20
k=7
for i in range(k,n):
    if a[i-k]%2==0:mchet=max(mchet,a[i-k])
    else:m=max(m,a[i-k])

    if a[i]%2!=0: ans=max(ans, a[i]*m)

print(ans)