def f(n):
    if n<5: return 0
    elif n==5: return 1
    elif n%3==0: return f(n-3)+f(n//3)
    else: return f(n-3)
print(f(27))
