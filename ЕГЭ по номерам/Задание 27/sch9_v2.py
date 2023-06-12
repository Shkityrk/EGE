f=open('schelchok/9_B__1vjy9.txt')
n=int(f.readline())
k=6
a=[int(x) for x in f.readlines()]
s=[-10**20]*8
mx=-10**20

for i in range(k,n):
    ost=a[i-k]%8
    s[ost]=max(s[ost], a[i-k])

    for j in range(len(s)):
        if (a[i]*s[j])%8==0 :
            mx=max(mx,a[i]*s[j] )
print(mx)