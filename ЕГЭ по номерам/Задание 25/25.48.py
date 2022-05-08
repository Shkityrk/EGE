def divs (n):
    s=[]
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s.append(d)
            s.append(n//d)
    return sorted(s)

for i in range(300_000_001, 300_050_000):
    f=divs(i)
    if len(f)>=5:
        p=f[0]*f[1]*f[2]*f[3]*f[4]
        if p%100==31 and p<=i:
            print(p, f[4])