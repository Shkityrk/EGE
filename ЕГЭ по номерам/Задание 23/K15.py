def f(c,e):
    if c>e: return 0
    if c==e: return 1
    if c<e and c%10!=9: return f(c+1,e)+f(c+11,e)
    if  c<e and c%10==9: return f(c+1,e)+f(c+10,e)
print(f(25,51))