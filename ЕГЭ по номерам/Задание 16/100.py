from functools import lru_cache
@lru_cache
def f(n):
    if n<=3: return n+3
    if n>3 and f(n-1)%2==0: return f(n-2)+n
    else: return f(n-2)+2*n
k=0
for n in range(40,51):
    k+=f(n)
print(k)