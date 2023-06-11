f=open('files_compege/27A_2755.txt')
n=int(f.readline())
mn=10**20
m=[10**20]*144

for i in range(n):
    x=int(f.readline())
    ost=0 if x%144==0 else 144-x%144

    if m[ost]<x and x+m[ost]<mn:
        mn=x+m[ost]
    m[x%144]=min(m[x%144],x)
print(mn)