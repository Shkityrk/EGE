def f(c,e,p1,p2):
    if c>e:return 0
    if c==e:return 1
    if c < e and p1==p2=='+1':return f(c*2,e,'*2',p1)
    if c < e and p1 == p2 == '*2': return f(c +1, e, '+1', p1)
    if c<e: return f(c+1,e,'+1',p1)+f(c*2,e,'*2',p1)

print(f(1,16,'',''))