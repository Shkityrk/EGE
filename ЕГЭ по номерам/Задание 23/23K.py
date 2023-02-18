def f(c,e,s):
    if c>e: return 0
    if c==e: return 1
    if c<e and s<=3: return f(c+2,e,s)+f(c*3,e,s+1)+f(c*5,e,s+1)
print(f(2,200,0))