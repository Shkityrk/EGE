def f(n):
    if n>20: return n**3+n
    elif n<=20 and n%2==0: return 3* f(n+1)+f(n+3)
    else: return f(n+2)+2*f(n+3)
k=0
for n in range(1,1001):
    x=f(n)
    z=1
    while x!=0:
        if x%10==1:
            z=0
        x//=10
    if z==1:k+=1
print(k)