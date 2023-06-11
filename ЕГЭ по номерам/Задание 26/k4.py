f=open('files_kompege/26_1079.txt')
n=int(f.readline())
a=[int(x) for x  in f.readlines()]
a.sort()

ans=[]
for i in range(n):
    for j in range(i+1,n):
        if (a[i]+a[j])%2==0:
            r=(a[i]+a[j])//2
            if a[2499]<r<a[3750]:
                ans.append(r)
print(len(ans), min(ans))