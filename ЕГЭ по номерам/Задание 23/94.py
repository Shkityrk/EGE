def f(n):
    if n>23: return 0
    elif n==22: return 1
    else: return f(n+1)+f(n+3)+f(n*4)
print(f(22))
