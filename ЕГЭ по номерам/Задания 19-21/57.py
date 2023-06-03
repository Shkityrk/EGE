def f(a,b,m):
    if a+b>=129:return m%2==0
    if m==0:return 0
    h=[f(a+1,b,m-1),f(a,b+1,m-1),f(a*4,b,m-1),f(a,b*4,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print('20' , [s for s in range(1,125) if not f(s,4,2) and f(s,4,3)])
print('21' , [s for s in range(1,125) if not f(s,4,3) and f(s,4,4)])


def f(a,b,c,m):
    if a+b>=129:return c%2==m%2
    if c>m:return 0
    h=[f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*4,b,c+1,m),f(a,b*4,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for a in range(1,125):
    for m in range(1,5):
        if m==4:
            if f(a,4,0,m):
                print(a,m)
                break
