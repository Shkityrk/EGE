start,end = 248015, 251575

def kol_divs(n):
    kol=1
    for v in range(1,round(int(i**0.5))):
        if n%v==0:
            kol+=1
    return kol

for i in range(start,end+1):
    if i%2!=0:
        kkk=kol_divs(i)
        if kkk%2!=0:
            print(i-248014, i, kkk, i**0.5 )