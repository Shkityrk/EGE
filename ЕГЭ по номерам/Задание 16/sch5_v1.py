def f(n):
    if n<=15:return n
    if 15<n<=25:return f(n-15)+n//3
    if n>25:return f(n-6)
print(f(20))