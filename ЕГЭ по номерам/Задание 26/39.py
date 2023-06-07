f=open('data/26-39.txt')
n,m=map(int, f.readline().split())
a=sorted([int(x) for x in f])

b=[]
for i in range(n):
    if 180<=a[i]<=200:
        b.append(a[i])
        a[i]=0
a=[int(x) for x in a if x!=0]

m=m-sum(b)
c=[]
while sum(c)+a[0]<=m:
    c.append(a.pop(0))
print(b,c)

c.sort(reverse=1)
for i in range(len(c)):
    for j in range(len(a)):
        if a[j]>c[i] and sum(c)-c[i]+a[j]<=m:
            