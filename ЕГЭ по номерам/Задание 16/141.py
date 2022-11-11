import math
import sys
sys.setrecursionlimit(10000)

def f(n):
    if n>=5000: return math.factorial(n)
    if n>=1 and n<5000: return 2*f(n+1)//(n+1)
print(1000*f(7)//f(4))