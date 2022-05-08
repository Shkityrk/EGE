start,end=190061, 190080
for i in range(start,end+1):
    a=[]
    for d in range(1,i+i,2):
        if i%d==0:
            a.append(d)
    if len(a)==4:
        print(*a[::-1])