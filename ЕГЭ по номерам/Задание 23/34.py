def f(n):
    if n<2: return 0
    elif n==2: return 1
    elif n%2==0: return f(n//2)+f(n-1)
    else: return f(n//2)+f(n-1)
print(f(16))
