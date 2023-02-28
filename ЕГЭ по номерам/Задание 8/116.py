from itertools import product
k=0
for x in product('АДЖИК', repeat=6):
    s=''.join(x)
    if not 'АА' in s and s.count('Д')==1 \
       and s.count('А')==2 and s.count('Ж')==1 and s.count('И')==1 \
       and s.count('К')==1: 
        k+=1
print(k)
