f=open('course/6.txt')
n=int(f.readline())
k=17

a=[int(x) for x in f.readlines()]
ans=0
for i in range(n):
    for j in range(i+1,n):
        for l in range(j + 1, n):
            if l-j>=17 and j-i>=17:
                s=a[i]+a[j]+a[l]
                if s%7717==0:ans+=1
print(ans)