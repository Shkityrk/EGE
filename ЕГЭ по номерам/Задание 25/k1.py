def d(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    return sorted(s)
for n in range(174457,174506):
    if len(d(n))==2:
        print(*d(n))