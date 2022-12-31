with open ("data/17-3.txt") as f:
    a=[int(x) for x in f.readlines()]
k=0
mx=0
for i in range(2,len(a)):
    if (a[i-2]+a[i-1]+a[i])%10==5 and (a[i-2]*a[i-1]*a[i])%7==0:
        k+=1
        mx=max(mx,a[i-2]+a[i-1]+a[i])
print(k,mx)