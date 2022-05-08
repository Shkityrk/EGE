start, end = 190201, 190280

for i in range(start,end+1):
    s=[]
    if i%2==0: s.append(i)
    for d in range(1,i//2+1):
        if i%d==0 and d%2==0:
            s.append(d)
            if len(s)>4: break
    if len(s)==4:
        print(*reversed(sorted(s)))

