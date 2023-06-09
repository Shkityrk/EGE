f=open('course/3.txt')
n=int(f.readline())
k=int(f.readline())
a=[int(x) for x in f.readlines()]
ans=0

for i in range(n):
    for j in range(i+1,n):
        if j-i>=k and abs(a[i]-a[j])%100==0 and \
                ((a[i]%37==0)+(a[j]%37==0))==1:
            ans+=1
print(ans)