start, end = 248015, 251575

def divs(n):
    kol=1
    for d in range(1, n//2+1):
        if n%d==0:
            kol+=1
    return kol

n=0
for i in range(start,end+1,2):
    m=divs(i)
    if m%2!=0:
        n+=1
        print (n,i, m, int(i**0.5) )