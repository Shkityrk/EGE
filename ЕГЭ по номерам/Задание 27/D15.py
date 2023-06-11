f=open('files_compege/27B_2754.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
ans=0
for i in range(n):
    for j in range(i+1,n):
        if j-i>=5 and abs(a[i]-a[j])%137==0:
            ans=max(ans,a[i]-a[j])
print(ans)