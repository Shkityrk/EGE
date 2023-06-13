def f(s,m):
    if s>=71:return m%2==0
    if m==0:return 0
    h=[f(s+1,m-1),f(s*3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print('19', [x for x in range(1,71) if f(x,2)])
print('20', [x for x in range(1,71) if f(x,3) and not f(x,1)])
print('21', [x for x in range(1,71) if f(x,4) and not f(x,3)])