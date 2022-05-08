
for n in range(126849, 126871+1):
    a=[]
    for d in range(1, n+1):
        if n%d==0:
            a.append(d)
            if len(a)>4:break
    if len(a)==4:
        print(*a)