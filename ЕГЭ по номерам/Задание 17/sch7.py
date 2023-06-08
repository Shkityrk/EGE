f=open('schelchok/7__1vf5c.txt')
a=[int(x) for x in f.readlines()]
sr=sum(a)//len(a)
ans=[]

def f(x):
    if x%14==0:return 1
    else:return 0
def g(x):
    if x<sr:return 1
    else:return 0

for i in range(2,len(a)):
    if (f(a[i-2]) or f(a[i-1]) or f(a[i])) and (g(a[i-2]) or g(a[i-1]) or g(a[i])):
        ans.append(a[i-2]+a[i-1]+a[i])
print(len(ans), max(ans))