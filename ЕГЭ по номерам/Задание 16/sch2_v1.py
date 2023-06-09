def f(n):
    if n==2:return 2
    if n>2:return f(n-1)*(n+4)
print(f(11)//f(7))