def f(c,e,s):
    if c>e: return 0
    if c==e and s!=6: return 0
    if c==e and s==6: return 1
    if c<e: return f(c+1,e,s+1)+f(c+2,e,s+1)+f(c*2,e,s+1)
print(f(1,20,0))