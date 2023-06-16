f=open('27B__1vpyj.txt')
r=int(f.readline())
a=[int(x) for x in f.readlines()]
mx=0
a.sort(reverse=True)
a=a[:800]
n=len(a)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if ((a[i]%17!=0)+ (a[j]%17!=0)+ (a[k]%17!=0))>=2:
                mx=max(mx, a[i]+a[j]+a[k])
print(mx)