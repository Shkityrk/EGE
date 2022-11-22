from functools import *
@lru_cache(None)
def f(n):
    if n>30: return n*n+5*n+4
    if n%2==0: return f(n+1)+3*f(n+4)
    else: return 2*f(n+2)+f(n+5)
l=0
for n in range(1,1001):
    try:
        s=str(f(n))
        if sum(int(k) for k in s)==27:l+=1
    except:pass
print(l)