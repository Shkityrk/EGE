def f(a,c,m):
    if a>=65:return c%2==m%2
    if c==m: return 0
    h=[f(a+1,c+1,m),f(a+2,c+1,m),f(a*3,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for a in range(1,65):
    for m in range(1,5):
        if f(a,0,m)==1:
            if m==2:print(a,m)
            break