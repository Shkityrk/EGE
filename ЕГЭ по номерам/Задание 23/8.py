def f(n):
    if n<1: return 0
    elif n==1: return 1    
    elif n%3==0: return f(n//3)+f(n-3)+f(n-1)
    else: return f(n-1)+f(n-3)
print(f(15))
