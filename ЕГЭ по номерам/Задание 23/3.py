def f(n):
    if n==1: return 1
    elif n%6==0: return f(n-1)+f(n//2)+f(n//3)
    elif n%2==0: return f(n-1)+f(n//2)
    elif n%3==0: return f(n-1)+f(n//3)
    else: return f(n-1)
print(f(18))
