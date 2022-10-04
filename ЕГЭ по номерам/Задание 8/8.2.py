from itertools import product

k=0
for x in product('ЭЮЯ','АБВГД','АБВГД','АБВГД','АБВГД'):
    s=''.join(x)
    k+=1
print(k)