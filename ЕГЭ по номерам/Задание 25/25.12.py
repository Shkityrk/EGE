start, end= 20789, 35672
for n in range(start,end+1):
    a=[]
    for d in range(1,n+1):
        if n%d==0:
            a.append(d)
    if len(a)==5:
        print(*a)