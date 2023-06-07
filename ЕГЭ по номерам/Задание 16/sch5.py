def f(n):
    if n==1:return 3
    if n==2:return 6
    if n==3:return 9
    if n>3:return f(n-3)*n+2
print(f(12))