f=open('27-148b.txt')
n=int(f.readline())
k=int(f.readline())
a=[int(x) for x in f .readlines()]

k157=k0=10**20

ans=10**20
for i in range(k,n):
    if a[i-k]%157==0:k157=min(k157,a[i-k])
    else:k0=min(k0,a[i-k])

    if a[i]%157==0:ans=min(ans, k157*a[i], k0*a[i] )
    else: ans=min(ans,k157*a[i] )
print(ans)