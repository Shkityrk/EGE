start=100812
end=100923
for i in range(start,end+1):

    a=[]
    for d in range(1,i+1):
        if i%d==0:
            a.append(d)

    if len(a)==6:
        print(*a)