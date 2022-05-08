st=190201
end=190230
for i in range(st,end+1):
    a=[]
    for d in range(1,i+1):
        if i%d==0:
            a.append(d)
    if len(a)==4:
        print(*a[::-1])