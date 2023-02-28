from itertools import product
k=0
for x in product('ТАР', repeat=6):
    s=''.join(x)
    if s.count('Т')==2 \
       and s.count('А')==2 and s.count('Р')==2:
        k+=1
print(k)
