start,end=2532000, 2532160
def divs(x):
    s=[]
    s.append(x)
    for d in range(1,int(x**0.5)):
        if x%d==0:
            s.append(d)
    return sorted(s)
kol=0
for i in range(start,end+1):
    n=divs(i)
    if len(n)==2:
        if i%10==7:
            kol+=1
            print(kol, i)