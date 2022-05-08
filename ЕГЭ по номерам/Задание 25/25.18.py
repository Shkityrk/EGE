start,end= 286564, 287270

def all_divs(x):
    a=[1,x]
    d=2
    while d**2<=x:
        if x%d==0:
            a.append(d)
            if x // d > d:
                a.append(x // d)
        d += 1
    return sorted(a)


mx_divs=[]
for x in range(start,end+1):

    if len(all_divs(x))>len(mx_divs):
        mx_divs=all_divs(x)
print(len(mx_divs),mx_divs[-1],mx_divs[-2])