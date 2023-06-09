f=open('course/8.txt')
n=int(f.readline())
k=int(f.readline())

a=[int(x) for x in f.readlines()]
ans=0
for i in range(n):
    for j in range(i+1,n):
        if j-i<=k:
            if  (a[i] + a[j])%17==0 :ans+=1
print(ans)