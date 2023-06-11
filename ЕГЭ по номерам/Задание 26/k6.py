f=open('files_kompege/26_2652.txt')
n=int(f.readline())

a=[int(x) for x in f.readlines()]
ans=[]

b=set(a)
d={c:0 for c in b}

for i in range(n):
    d[a[i]]+=1
print(max(d.values()))