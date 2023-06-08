f=open('schelchok/2__1vf54.txt')
a=[int(x) for x in f.readlines()]
r=[]
ans=[]
for i in range(len(a)):
    if a[i]%6==0:r.append(a[i])
sr=sum(r)//len(r)

for i in range(1,len(a)):
    if ((a[i-1]>sr) +(a[i]>sr))==1:ans.append(a[i-1]+a[i])
print(len(ans), max(ans))