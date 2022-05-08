start=81234
end=134689

def divs(n):
    div=set()
    for d in range(1,int(n**0.5)+1):
        if n%d==0:
            div.add(d)
            div.add(n//d)
    return sorted(div)

for i in range(start,end+1):
    d=divs(i)
    if len(d)==5:
        print(d[1],d[-2])