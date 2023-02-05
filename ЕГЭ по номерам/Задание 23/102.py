def f(c,e):
    if c>e or c==8: return 0
    if c==e: return 1
    if c<e: return f(c+1,e)+f(c+4,e)+f(c*4,e)
print(f(2,6)*f(6,24))