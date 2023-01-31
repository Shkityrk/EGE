def f(n):
    if n<2: return 0
    elif n==2: return 1
    elif int(n**0.5)**2==n: return f(int(n**0.5))+f(n-3)+f(n-1)
    else: return f(n-3)+f(n-1)
print(f(19))
