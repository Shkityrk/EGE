from itertools import product
k=0
for x in product('АГИЛМОРТ',repeat=4):
    s=''.join(x)
    k+=1
    if s[-2]=='И' and s[-1]=='М':
        print(k,*s)