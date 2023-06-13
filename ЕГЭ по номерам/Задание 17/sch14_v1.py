f=open('schelchok/17__1ssmj.txt')
a=[int(x) for x in f.readlines()]

mn=10**20
ans=[]
for i in range(len(a)):
    if len(str(a[i]))==3 and a[i]%10==3:mn=min(mn,a[i])

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]+a[j])%mn==0 and ((len(str(a[i]))==3) +(len(str(a[j]))==3))==1 :
            ans.append(a[i]+a[j])
print(len(ans), min(ans))