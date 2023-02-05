'''def f(n):
    if n<0: return 0
    elif n==1: return 1
    elif n%3==0: return f(n//3)+f(n-1)+f(n-3)
    else:return (n-1)+f(n-3)
print(f(34))'''
def f(c,e):
    if c>e: return 0
    if c==e: return 1
    else: return f(c+3,e)+f(c+1,e)+f(c*3,e)
print(f(1,34))
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!