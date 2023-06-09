f=open('course/4.txt')
n=int(f.readline())
ans=10**10
a=[int(x) for x in f.readlines()]

for i in range(n):
    for j in range(i+1,n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):
                if (a[i]+a[j]+a[k]+a[l])%9==0:ans=min(ans,a[i]+a[j]+a[k]+a[l])
print(ans)
