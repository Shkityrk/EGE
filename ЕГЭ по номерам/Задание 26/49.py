f=open('data/26-49.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
a.sort()
med=n//2
ans=[]
for i in range(n):
    for j in range(i+1,n):
        if (a[i]+a[j])%2==0:
            sr=(a[i] + a[j]) // 2
            if sr<a[med]:
                ans.append(sr)
print(len(ans), max(ans))