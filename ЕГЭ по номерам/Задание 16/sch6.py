def f(n):
    if n<=1:return 1
    if n%2!=0:return f(n-2)+n*n
    else:return f(n-1)+n
print(f(80))