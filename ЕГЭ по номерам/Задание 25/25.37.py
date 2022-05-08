start, end = 678220, 679335
mx_sum=0
kol=0
def divs(n):
    s=[]
    for d in range(1, n//2+1):
        if n%d==0:
            s.append(d)
    return sorted(s)

for i in range(start,end+1):
    d=divs(i)
    if len(d)<=4:
        if sum(d)>mx_sum:
            mx_sum=sum(d)
            kol+=1
print(mx_sum,kol)


