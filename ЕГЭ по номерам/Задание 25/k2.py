def d(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    return sorted(set(s))
for n in range(81234,134689):
    if len(d(n))==3:
        print(*d(n))