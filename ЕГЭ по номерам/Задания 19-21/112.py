def f(s,m):
    if s>=82:return m%2
    if m==0:return 0
    h=[f(s+10,m-1),f(s*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print('19',[s for s in range(1,82) if f(s,3)])