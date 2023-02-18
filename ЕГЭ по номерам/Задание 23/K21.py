def f(c,e,p):
    if c>e: return 0
    if c==e: return 1
    if c<e and p=='*2': return f(c+1,e,'+1')+f(c+2,e,'+2')
    if c < e and p != '*2': return f(c + 1, e, '+1') + f(c + 2, e, '+2')+ f(c * 2, e, '*2')
print(f(1,15,''))