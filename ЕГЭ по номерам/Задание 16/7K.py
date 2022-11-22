def f(n):
    if n<=3: return 3
    if n%2==0: return f(n//2)+5
    else: return f(n-1)-f(n-2)
print(f(20))