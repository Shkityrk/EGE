f=open('schelchok/17__1ssk3.txt')
a=[int(x) for x in f.readlines()]
mn=10**20
ans=[]

for i in range(len(a)):
    if a[i]%24==0:mn=min(mn,a[i])

for i in range(1,len(a)):
    if a[i-1]%mn==0 or a[i]%mn==0:
        ans.append(a[i-1]+a[i])
print(len(ans),max(ans))