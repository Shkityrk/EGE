def f(n):
    mx=0
    mn=10
    while n!=0:
        mx=max(n%10, mx)
        mn = min(n % 10, mn)
        n//=10
    return (mx-mn)
k=0
for n in range(147870,1005-1,-1):
    if '1' not in str(n) and f(n)<4:
        k+=1
        if k<30:print(k,n)

print(k)