f=open('27-147b.txt')
n=int(f.readline())
k=int(f.readline())
a=[int(x) for x in f.readlines()]

m=[-10**20]*101
mx=-10**20

for i in range(k,n):
    ost= a[i-k]%101
    m[ost]=max(m[ost],a[i-k])

    ost2=0 if a[i]%101==0 else 101-a[i]%101
    su=m[ost2]+a[i]
    mx=max(mx,su)
print(mx)