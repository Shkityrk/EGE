f=open('schelchok/27-9b__1vjmq.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
mn=[10**20]*7

ans=10**20
for i in range(n):
    x=a[i]
    ost2=0 if x%7==0 else 7-x%7
    ans=min(ans, x+mn[ost2])

    ost=x%7
    mn[ost]= min(mn[ost], x)
print(ans)
