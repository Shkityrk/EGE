f=open('schelchok/27-5b__1vjmh.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
a.sort(reverse=True)
mx=-10**20
l=a[:5000]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if (a[i]*a[j])%27==0 and (a[i]*a[j])%2==0:
            mx=max(mx, a[i]*a[j])
print(mx)