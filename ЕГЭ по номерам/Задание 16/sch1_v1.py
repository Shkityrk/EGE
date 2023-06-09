def f(n):
    if n>1000:return n
    if n<=1000:return 7*n**2+3+f(n+1)

print(f(6)-f(12))