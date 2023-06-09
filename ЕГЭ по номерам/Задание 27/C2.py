f=open('course/2.txt')
n=int(f.readline())
k=int(f.readline())
a=[int(x) for x in f.readlines()]
ans=0

for i in range(n):
    for j in range(i,n):
        if j-i>=k:
            if  (a[i]+a[j])%2023==0 and (a[i]%47==0)+(a[j]%47==0)==1:ans=max(ans,a[i]+a[j])
print(ans)