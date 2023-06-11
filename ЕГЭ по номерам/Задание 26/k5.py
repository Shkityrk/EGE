f=open('files_kompege/26_1257.txt')
n=int(f.readline())
ans=[]
a=[int(x) for x in f.readlines()]
b=set(a)

for i in range(n):
    for j in range(i+1,n):
        if a[i]%2!=a[j]%2 and (a[i]+a[j]) in b:
            ans.append(a[i]+a[j])
print(len(ans), max(ans))