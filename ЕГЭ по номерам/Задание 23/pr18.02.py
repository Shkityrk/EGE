def f(c,e,k1,k2,k3):
    if c>e: return 0
    if c==e: return 1
    if c<e: return f(c*5,e)+f(c*3,e)+f(c+45,e)
print(f(1))