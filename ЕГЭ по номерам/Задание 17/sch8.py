f=open('schelchok/8__1vf5e.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(1,len(a)):
    if (a[i-1]%5==0 or a[i]%5==0) and (a[i-1]+a[i])%10==0:
        ans.append(a[i-1]+a[i])
print(len(ans), max(ans))