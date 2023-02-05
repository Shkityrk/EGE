def f(c,e):
    if c<e: return 0
    if c==e: return 1
    else: return f(c-8,e)+f(c//2,e)
print(f(102,43)*f(43,5))