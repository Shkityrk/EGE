def f(s,m):
    if s>=38:return m%2==0
    if m==0:return 0
    h=[f(s+2,m-1),f(s*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print('21', [s for s in range(1,38) if f(s,4) and f(s,3)==0])