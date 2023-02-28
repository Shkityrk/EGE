m=0
for i in range(394441, 394505+1):
    k=[]
    for d in range(1,int(i**0.5)+1):
        if i%d==0:
            k.append(d)
            k.append(i//d)
    m=max(m,len(k))
for i in range(394441, 394505+1):
    k=[]
    for d in range(1,int(i**0.5)+1):
        if i%d==0:
            k.append(d)
            k.append(i//d)
    k=sorted(k)       
    if len(k)==m:
        print(m,k[-2],k[-1])
        break
