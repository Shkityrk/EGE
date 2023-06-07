def f(s,m):
    if s>=29:return m%2==0
    if m==0:return 0
    h=[f(s+1,m-1), f(s*2,m-1),f(s+2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print('19', [s for s in range(1,29) if f(s,2)])
print('20', [s for s in range(1,29) if f(s,3) and f(s,1)==0])
print('21', [s for s in range(1,29) if f(s,4) and f(s,3)==0])