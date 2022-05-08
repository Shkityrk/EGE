start, end = 100806, 100950
for i in range(start,end+1):
    s=[]
    s.append(i)

    for d in range(1,i//2+2):
        if i%d==0:
            s.append(d)
        if len(s)>6:break
    if len(s)==6:
        print(*sorted(s))