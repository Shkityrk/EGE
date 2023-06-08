f=open('schelchok/5__1vf59.txt')
a=[int(x) for x in f.readlines()]
ans=[]
sr=sum(a)//len(a)
def f(x):
    return 1 if abs(x)%2==0 else 0

for i in range(2,len(a)):
    if f(a[i-2])+f(a[i-1])+f(a[i])==1 and (max(a[i-2],a[i-1],a[i])+min(a[i-2],a[i-1],a[i]))>sr:
        ans.append(a[i-2]+a[i-1]+a[i])


print(len(ans), max(ans))