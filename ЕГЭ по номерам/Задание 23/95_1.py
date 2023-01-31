def f(n):
    if n<2 or n==14: return 0
    if n==2: return 1
    elif n==11 or n==10: return f(n-1)
    else: return f(n-1) +f(n-3)

print(f(18))
