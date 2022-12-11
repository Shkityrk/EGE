def f(n):
    s=0
    while n!=0:
        s+=n%10
        n//=10
    return s
k=0
mx=0
for n in range(3912, 9194):
    if f(n)%9==0 and n%256!=33:
        k+=1
        mx=max(mx,n)
print(k,mx)