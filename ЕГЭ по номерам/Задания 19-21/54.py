def f (a,b,c,m):
    if a+b>=83: return c%2==m%2
    if c==m: return 0

    h=[f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*4,b,c+1,m),f(a,b*4,c+1,m), ]
    return any(h) if (c+1)%2==m%2 else any(h)

for b in range(1,77):
    for m in range(1,5):
        if f(5,b,0,m)==1:
            if m==2:print(b,m)
            break