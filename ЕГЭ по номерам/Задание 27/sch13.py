f=open('schelchok/27-13b__1vjmy.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
s=[0]*12
ans=-10**20
for i in range(n):
    ost=a[i]%12

    ost2=0 if a[i]%12==0 else 12-a[i]%12
    ans=max(ans, a[i]+s[ost2])

    s[ost]=max(s[ost], a[i])
print(ans)