f=open('data/26-52.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
ma=float('inf')
a.sort()
k=0
for i in range(n-1):
    for j in range(i+1,i+2+100):
        if j< n and (a[i]+a[j])%10==0:
            k+=1
            ma = min( ma, (a[i]+a[j])//2 )
print(k,ma)