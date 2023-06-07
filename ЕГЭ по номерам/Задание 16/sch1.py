def f(n):
    if n>=670:return n-5
    if n<670:return 5*n+7+f(5*n+7)
print(f(600)-f(300))