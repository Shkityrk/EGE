def f(a,c,m):
    if a>=25: return c%2==m%2
    if c==m:return 0
    h=[f(a+3,c+1,m),f(a*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
k=0
for a in range(1,25):
    for m in range(1,5):
        if f(a,0,m)==1:
            if m==2:
                print(a,m)
                break