def d(n):
    s=[]
    s.append(1)
    s.append(n)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    return sorted(set(s))
for n in range(154026,154044):
    if len(d(n))==4:
        print(*d(n)[2:])