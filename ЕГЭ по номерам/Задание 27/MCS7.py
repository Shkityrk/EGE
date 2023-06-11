f=open('files_compege/27B_2900.txt')
n=int(f.readline())
m=[10**20]*1000
s=ms=0
for i in range(n):
    x=int(f.readline())
    s+=x
    if s%1000==0:ms=max(ms,s)
    ms=max(ms,s-m[s%1000])

    m[s%1000]=min(m[s%1000],s)
print(ms)