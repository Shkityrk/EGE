f=open('27-149a.txt')
n=int(f.readline())
k=int(f.readline())
a=[int(x) for x in f.readlines()]
mxA=-10**20
for i in range(n):
    for j in range(i+1,n):
        if j-i>=k and ((a[i]%47==0)+(a[j]%47==0))==1 and (a[i]+a[j])%2023==0:
            mxA=max(mxA, a[i]+a[j])



k47=[-10**20]*2023
k0=[-10**20]*2023
mxB=-10 ** 20

for i in range(k,n):
    ost=a[i-k]%2023
    if a[i-k]%47==0:k47[ost]=max(k47[ost], a[i-k])
    else:k0[ost]=max(k0[ost], a[i-k])

    ost2=0 if a[i]%2023==0 else 2023-a[i]%2023
    if a[i]%47==0:
        mxB=max(mxB, k0[ost2] + a[i])
    if a[i] % 47 != 0: mxB=max(mxB, k47[ost2] + a[i])
print(mxA==mxB)