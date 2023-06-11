
f=open('files_compege/27B_2764.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
k=7
mn=10**20
for i in range(k,n):
    f=a[:i-7]
    for j in range(len(f)):
        if (a[i]+f[j])%23==0 and (a[i]*f[j]%6)==0:mn=min(mn,(a[i]+f[j]))
print(mn)