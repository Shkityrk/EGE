f=open('data/26-45.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
b=set(a)
ans=[]
for i in range(n):
    for j in range(i+1,n):
        if (a[i]+a[j])%2==0:
            sr=(a[i]+a[j])//2
            if sr in b:ans.append(sr)
print(len(ans),max(ans))
