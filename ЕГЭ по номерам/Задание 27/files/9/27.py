f=open('27-9b.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]

m_nch=10**20

ans=10**20

for i in range(6,n):
    if a[i-6]%2!=0: m_nch=min(m_nch,a[i-6])

    if a[i]%2!=0:ans=min(ans, a[i]*m_nch)
print(ans)