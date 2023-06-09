def f(n):
    if n<100:return 5+n+f(n+2)
    if n>=100:return n+2
print(f(90)-f(101))