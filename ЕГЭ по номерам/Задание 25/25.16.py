st,end=394441, 394505
mx=0
for i in range(st,end+1):
    kol=0
    for d in range(1,i+1):
        if i%d==0:
            kol+=1
    if kol>mx:
        mx=kol

for i in range(st,end+1):
    koll=0
    a=[]
    for d in range(1,i+1):
        if i%d==0:
            koll+=1
            a.append(d)
    if koll==mx:
        print(mx, i, *a[-2:-1])
        break