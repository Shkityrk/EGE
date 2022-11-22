def f(n):
    if n==1: return 1
    if n==2: return 2
    if n%2==0: return (n+f(n-2))//5
    else: return (2*n+f(n-1)+f(n-2))//4
print(f(100))