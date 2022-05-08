start=int(244143**0.5)
end= int((367821+1)**0.5)
for i in range(start,end):
    n=i**2
    a=[]
    for d in range(1,n+1):
        if n%d==0:
            a.append(d)

    if len(a)==5:
        print(a)