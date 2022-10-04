from itertools import product
k=0
for x in product('ЛТ','ЛЕТО','ЛЕТО','ЛЕТО',):
    s=''.join(x)
    k+=1

print(k)
