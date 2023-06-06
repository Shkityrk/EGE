f=open('...')
s,n=map(int, f.readline().split())
a=[int(x) for x in f]
a.sort()

s1=0
k=0
for i in range(n):
    if s1+a[i]<=s:
        s1+=a[i]
        k+=1
        a[i]=0
print(s1,k)