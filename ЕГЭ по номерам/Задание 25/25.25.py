start,end=194441, 196500

def divs(n):
    s=[]
    s.append(n)
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
    return s
kol=0
for i in range(start,end+1):
    kol+=1
    if len(divs(i))%2!=0:
        print(kol, i,len(divs(i)), int(i**0.5))