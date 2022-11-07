def f(n):
    if n<=1: return n*n
    if n>1: return  n*n+ 2*n+1+ f(n-2)+f(n//3)
for n in range(1,10000):
    if f(n)>3200000:
        print(n, f(n))
        break