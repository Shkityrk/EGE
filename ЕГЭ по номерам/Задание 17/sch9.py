f=open('schelchok/9__1vf5f.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(1,len(a)):
    if (a[i-1]+a[i])%134==0:
        ans.append(a[i-1]+a[i])
print(len(ans), max(ans))