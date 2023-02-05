def f(c,e):
    if c>e or c==18 or c==11: return 0
    if c==e: return 1
    if c<e: return f(c+1,e)+f(c+2,e)+f(c*3,e)
print(f(4,8)*f(8,23))