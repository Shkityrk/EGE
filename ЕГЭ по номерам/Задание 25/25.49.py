def divs(n):
    s=[]
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s.append(d)
            s.append(n//d)
    return sorted(s)


for i in range(500_000,600_000):
    d=divs(i)
    for d1 in range(len(d)):
        if d[d1]%10==8 and d[d1]!=8 and d[d1]!=i:
            print(i, d[d1])
            break