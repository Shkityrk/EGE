def f(n):
    if n==1: return 1
    if n==2: return 2
    if n%2==0: return int((7*n+f(n-3))//9)
    else: return int((5*n+f(n-1)+f(n-2))//7)

print(f(50))