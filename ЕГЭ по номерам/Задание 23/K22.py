def f(c,e,p):
    if c>e: return 0
    if c==e: return p==1
    else: return f(c+1,e,p)+f(c+2,e,p)+f(c*2,e,p+1)
print(f(2,12,0))