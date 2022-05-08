start=102714
end=102725
for n in range(start,end+1):
    a=[]
    for d in range(1,n+1):
        if n%d==0:
            a.append(d)
        if len(a)>4: break
    if len(a)==4:
        print(*a)