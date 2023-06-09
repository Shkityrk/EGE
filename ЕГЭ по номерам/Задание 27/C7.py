f=open('course/7.txt')
n=int(f.readline())
m=34

a=[int(x) for x in f.readlines()]
ans=0
for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j] and (a[i] + a[j])<=m:ans+=1
print(ans)