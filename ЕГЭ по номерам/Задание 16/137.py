from sys import setrecursionlimit
setrecursionlimit(50000)
def F( n ):
    if n < 4 or n % 2 == 1: return 1
    else: return F(n-1) + F(n-2) + F(n-3)
print(F(2008)-F(2006))