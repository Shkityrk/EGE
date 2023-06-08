f=open('schelchok/4__1vf58.txt')
a=[int(x) for x in f.readlines()]
ans=[]
summ=max(a)+min(a)
def f(x):
    if x%10==3 or x%10==7:return 1
    else:return 0

for i in range(2,len(a)):
    if (f(a[i-2]) or f(a[i-1]) or f(a[i])) and (a[i-2]+a[i-1]+a[i])>summ:
        ans.append(a[i-2]+a[i-1]+a[i])

print(len(ans), max(ans))