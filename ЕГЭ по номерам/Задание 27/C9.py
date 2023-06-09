f=open('course/9.txt')
n=int(f.readline())
k=7

a=[int(x) for x in f.readlines()]
ans=10**10
for i in range(n):
    for j in range(i+1,n):
        if j-i>=k:
            if  (a[i]+a[j])%23==0  and (a[i]*a[j])%6==0:ans=min(ans,(a[i]+a[j]))
print(ans)