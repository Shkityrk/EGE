start,end=193136,193223
def divs(n):
    d=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
    return sorted(d)

for i in range(start,end+1):
    d=divs(i)
    if len(d)==6:
        print(*d)