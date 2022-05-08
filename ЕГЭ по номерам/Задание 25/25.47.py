def divs(n):
    s=[]
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s.append(d)
            s.append(n//d)
    return sorted(s)

for i in range(1500001, 1500100):
    l=divs(i)
    if l!=[]:
        F=sum(l) // len(l)
        if F%10==9:
            print(i, F)

