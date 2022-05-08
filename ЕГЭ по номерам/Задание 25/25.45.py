start, end = 333555 , 777999

def divs(n):
    s=[]
    d=2
    while d**2<=n:
        if n%d==0 and 10<=d<100:
            s.append(d)
            if n//d>d and 10<=n//d<100:
                s.append(n//d)

        d+=1
    return sorted(s)
for i in range(start,end+1):
    l=divs(i)
    if len(l)==35:
        print(i, l[0], l[-1])

