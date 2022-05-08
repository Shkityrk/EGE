start, end = 2, 30_000
def divs (n):
    s=[]
    for d in range(1,n//2+1):
        if n%d==0 and d!=n:
            s.append(d)
    return sorted(s)

num=0
for i in range(start,end+1):
    if i>sum(divs(i)):
        num+=1

print(num)