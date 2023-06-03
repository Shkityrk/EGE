'''from functools import lru_cache
@lru_cache
def f(n):
    if n==0: return 1
    if n>0: return 2*f(1-n)+3*f(n-1)+2
    if n<0: return -1*f(-1*n)
'''
cache={}
def f(n):
    if n not in cache:
        if n==0: cache[0]=1
        if n>0: cache[n]= 2*f(1-n)+3*f(n-1)+2
        if n<0: cache[n]= -1*f(-1*n)
    return cache[n]

print(f(50))
k=0
'''while n!=0:
    countA+=n%10
    n//=10
print(countA)
'''
