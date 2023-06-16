def divs(x):
    s=[]
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            s.append(i)
            s.append(x//i)
    s.sort()
    return s

for n in range(193136, 193223+1):
    d=divs(n)
    if len(d)==6:
        print(*d[-2:])