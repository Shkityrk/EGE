f=open('schelchok/27-7b__1vjmm.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
a.sort(reverse=True)

max7=-10**20
max0=-10**20
for i in range(n):
    if a[i]%7==0:max7=max(max7,a[i])
    else:max0=max(max0,a[i])
print(max7*max0)