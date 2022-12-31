with  open ("data/17-3.txt") as f:
    a=[int(x) for x in f.readlines()]
k=0
su=0
for i in range(1,len(a)):
    if (abs(a[i-1])%2==0 and abs(a[i-1])%4==0 and abs(a[i])%2!=0 and abs(a[i])%11==0) or\
       (abs(a[i-1])%2!=0 and abs(a[i-1])%11==0 and abs(a[i])%2==0 and abs(a[i])%4==0):
        k+=1
        su=max(su, a[i-1]+a[i])
print(k,su)
