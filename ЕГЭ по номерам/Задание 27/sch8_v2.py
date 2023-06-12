f=open('schelchok/8_B__1vjy7.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
k=4
s6=s3=s2=s=-10**20
ans=-10**20
for i in range(k,n):
    if a[i-k]%6==0: s6=max(s6,a[i-k])
    elif a[i - k] % 3 == 0: s3 = max(s3, a[i - k])
    elif a[i - k] % 2 == 0:s2 = max(s2, a[i - k])
    else: s = max(s, a[i - k])

    if a[i]%6==0: ans=max(ans, a[i]*s6, a[i]*s3, a[i]*s2,a[i]*s)
    elif a[i]%3==0:ans=max(ans, a[i]*s2)
    elif a[i]%2==0:ans=max(ans, a[i]*s3)
    else: ans=max(a[i]*s6, ans)
print(ans)