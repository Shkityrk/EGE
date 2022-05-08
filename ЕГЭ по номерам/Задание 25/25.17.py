st,end=286564, 287270
max_kol=0

for i in range(st,end+1):
    kol=0
    for d in range(1,i+1):
        if i%d==0:
            kol+=1
    if kol>max_kol:
        max_kol=kol

for i in range(end, st):
    a=[]
    kol = 0
    for d in range(1, i + 1):
        if i % d == 0:
            kol += 1
    if kol==max_kol:
        print(i, max_kol, a[-1:-2:-1])
