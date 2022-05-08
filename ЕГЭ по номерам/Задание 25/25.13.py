from math import sqrt as sq
start, end=125873, 136762
qstart=int(sq(start))
qend=int(sq(end+1))
for i in range(qstart,qend):
    n=i**2
    a=[]
    for d in range(1,n+1):
        if n%d==0:
            a.append(d)
    if len(a)==5:
        print(*a)