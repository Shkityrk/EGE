f=open('files_compege/27B_2900.txt')
n=int(f.readline())
ms=0
m=[10**20]*1000
s=0

for i in range(n):
    x=int(f.readline())
    s+=x
    if s%1000==0:ms=max(ms,s)

    s1=s-m[s%1000]
    ms=max(ms,s1)

    m[s%1000]=min(m[s%1000], s)
print(ms)