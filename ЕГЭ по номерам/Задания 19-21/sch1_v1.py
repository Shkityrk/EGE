def f(s,m,last):
    if s>=50:return m%2==0
    if m==0:return 0

    h=[]

    if last!='+2': h+=[f(s+2,m-1,'+2')]
    if last!='+1': h+=[f(s+1,m-1,'+1')]
    if last!='*3': h+=[f(s*3,m-1,'*3')]
    return any(h) if (m-1)%2==0 else all(h)

print('19', [s for s in range(1,50) if f(s,2,'')])
print('20', [s for s in range(1,50) if f(s,3,'')==1 and not f(s,1,'')])
print('21', [s for s in range(1,50) if f(s,4,'')==1 and not f(s,3,'')])