f=open('schelchok/3__1vf57.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(2,len(a)):
    if ((a[i-2]%2==0)+(a[i-1]%2==0)+(a[i]%2==0))>=2 and (a[i-2]+a[i-1]+a[i])%3==0:
        ans.append(a[i-2]+a[i-1]+a[i])
print(len(ans), min(ans))