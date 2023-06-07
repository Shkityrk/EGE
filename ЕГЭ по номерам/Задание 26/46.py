f=open('data/26-46.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
ans=[]
b=set(a)

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (a[i]+a[j]+a[k])%3==0:
                sr=(a[i]+a[j]+a[k])//3
                if sr in b:
                    ans.append(sr)
print(len(ans), min(ans))