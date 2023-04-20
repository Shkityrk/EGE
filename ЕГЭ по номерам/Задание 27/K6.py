f=open('files_compege/27B_2724.txt')
n=int(f.readline())
k=0
a=[int(x) for x in f.readlines()]
for x in range(n):
    for y in range(x+1,n):
        if (a[x]+a[y])%131==0:k+=1
    if 
print(k)