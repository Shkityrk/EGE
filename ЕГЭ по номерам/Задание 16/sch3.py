def f(n):
    if n==0:return 1
    if n==1:return 2
    if n>1:return 6*f(n-1)-f(n-2)
print(f(4))