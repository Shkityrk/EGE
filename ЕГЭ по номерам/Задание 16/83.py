from functools import lru_cache
@lru_cache
def f(n):
    if n<=5: return n
    if n>5 and n%8==0: return n+f(n/2-3)
    if n > 5 and n % 8 != 0: return n+f(n+4)
for n in range(1000,1,-1):
    try:
        if f(n):
            print(n)
            break
    except: pass