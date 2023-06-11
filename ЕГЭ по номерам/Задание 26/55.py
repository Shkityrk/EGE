f=open('data/26-55.txt')
n,s=map(int, f.readline().split())
a=[int(x) for x in f.readlines()]
a.sort()
b=[]

while sum(b)+a[0]<=s:
    b.append((a.pop(0)))
b.sort(reverse=1)
for i in range(len(b)):
    for j in range(len(a)):
        if a[j]>b[i] and sum(b)-b[i]+a[j]<=s:
            b[i], a[j]=a[j], b[i]
print(min(b), sum(b))