f=open('schelchok/10__1vf5g.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(1,len(a)):
    if abs(a[i]-a[i-1])%2==0 and (a[i-1]%11==0 or a[i]%11==0):
        ans.append(a[i-1]+a[i])
print(len(ans), min(ans))