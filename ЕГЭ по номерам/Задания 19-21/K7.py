def f(s,a,b,c,m):
    if s+a+b>=73:return c%2==m%2
    if c==m:return 0
    h=[f(s+3,a,b,c+1,m),f(s+13,a,b,c+1,m),f(s+23,a,b,c+1,m),
       f(s,a+3,b,c+1,m),f(s,a+13,b,c+1,m),f(s,a+23,b,c+1,m),
       f(s,a,b+3,c+1,m),f(s,a,b+13,c+1,m),f(s,a,b+23,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for s in range(1,24):
    for m in range(1,5):
        if f(2,s,2*s,0,m)==1:
            if m==4:print(s,m)
            break