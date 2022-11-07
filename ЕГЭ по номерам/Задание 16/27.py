def f(n):
    if n<=1: return n+1
    else: return n+1+2*n+f(n-1)+f(n-3)
for n in range(1,1000):
    if f(n)>1_000_000:
        print(n, f(n))
        break