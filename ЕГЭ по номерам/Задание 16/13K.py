from functools import *
@lru_cache(None)
def f(n):
    if n<=18: return n+3
    if n%3==0: return (n//3)*f(n//3)+n-12
    else: return f(n-1)+n*n+5

k=0
for n in range(1,1001):
    s=str(f(n))
    if all(k not in s for k in '13579'):k+=1
print(k)