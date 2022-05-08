start, end = 573213, 575340

def divs(n):
    s=[]
    s.append(n)
    for d in range(1,n//2+1):
        if n%d==0:
            s.append(d)
    return sorted(s)

min_summ=10000000000
min_list=[]

for i in range(start,end+1):
    all_divs=divs(i)
    if len(all_divs)==4:
        if sum(all_divs)<min_summ:
            min_summ=sum(all_divs)
            min_list=all_divs

print(min_summ, min_list[-2])

