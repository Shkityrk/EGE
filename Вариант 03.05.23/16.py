from functools import lru_cache
@lru_cache(None)
def f(n):
    if n>3000:return n
    if n<=3000 and n%2==0:return n+f(n+1)+1
    if n<=3000 and n%2!=0:return f(n+2)+2

print(f(40)-f(43))