def f(a,b,c,m):
    if a+b>=101:return c%2==m%2
    if c==m:return 0

    h=[f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for b in range(1,94):
    for m in range(1,5):
        if f(7,b,0,m)==1:
            if m==4:print(b,m)
            break