f=open('schelchok/1__1vf52.txt')
a=[int(x) for x in f.readlines()]
mx=0
ans=[]
for i in range(len(a)):
    if a[i]%15==0:mx=max(mx,a[i])

for i in range(1,len(a)):
    if a[i-1]>mx or a[i]>mx:
        ans.append(a[i-1]+a[i])
print(len(ans), min(ans))