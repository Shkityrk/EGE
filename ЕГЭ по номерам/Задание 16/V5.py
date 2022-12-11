def f(n):
    if n<=1: return 1
    if n%2!=0:return 5*n+f(n-1)+f(2)
    else: return 3*f(n-1)
print(f(23))