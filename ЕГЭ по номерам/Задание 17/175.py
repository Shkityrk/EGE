with open("data/17-4.txt") as f:
    a=[int(x) for x in f.readlines()]
k=0
c=0

for i in range(len(a)):
    b=a[i]
    su=0
    while b!=0:
        su+=b%10
        b//=10
    if su%5==0 and a[i]%9!=0:
        k+=1
        c=max(a[i], c)
print(k,c)
