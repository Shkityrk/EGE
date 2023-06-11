f=open('files_compege/27B_2758.txt')
n=int(f.readline())
a=[int(x) for x in f]
mn=10**20
for i in range(n):
    for j in range(i+1,n):
        if j-i>11:break
        if (a[i]+a[j])%2142==0:
            mn=min(mn,(a[i]+a[j]))
print(mn)