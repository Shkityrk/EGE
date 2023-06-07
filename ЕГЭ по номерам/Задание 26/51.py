f=open('data/26-51.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
a.sort()
mx=0
k=0
s=0
for i in range(n):
    for j in range(i+1,n):
        if j-i>100:
            if (a[i]+a[j])%2==0:
                k+=1
                if (a[i]+a[j])>mx:
                    mx=a[i]+a[j]
                    s=(a[i]+a[j])//2
print(k,s)