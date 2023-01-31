def f(n):
    if n<2 or n==14: return 0
    if n==2: return 1
    else: return f(n-1) +f(n-3)
def g(n):
    if n<2 or n==14 or n==9: return 0
    if n==2: return 1
    else: return g(n-1) +g(n-3)

print(f(18)-g(18))
