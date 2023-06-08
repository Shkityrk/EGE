f=open('schelchok/6__1vf5a.txt')
a=[int(x) for x in f.readlines()]
ans=[]
def f(x):
    return 1 if abs(x)%2==1 else 0
def g(x,y,z):
    return 1 if max(x,y,z)+ min(x,y,z)<0 else 0

for i in range(2,len(a)):
    if f(a[i-2])==1 and f(a[i-1])==1 and f(a[i])==1 and g(a[i-2],a[i-1],a[i])==1:
        ans.append(a[i-2]+a[i-1]+a[i])
print(len(ans), min(ans))