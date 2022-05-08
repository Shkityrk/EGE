start, end = 81234 , 134689

def divs(n):
    s=[]
    for d in range(2,n//2+1):
        if n%d==0:
            s.append(d)
            if len(s)>3:
                return [0]

    return s

for i in range(start,end + 1):
    list = divs(i)
    if len(list)==3:
        print(min(list), max(list))

