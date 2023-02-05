def f(c,e):
    if c>e or c ==21:return 0
    if c==e: return 1
    if c<e: return f(c*3,e)+f(c*4,e)+f(c+1,e)
print(f(2,16)*f(16,60))