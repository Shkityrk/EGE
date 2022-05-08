start,end=190201, 190280
for i in range(start,end+1):
    a=[]
    for d in range(2,i+1,2):
        if i%d==0:
            a.append(d)
    if len(a)==4:
        print(*a[::-1])