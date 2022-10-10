from itertools import product
k=0
for x in product('МАРТ', repeat=5):
    s=''.join(x)
    if not 'АА' in s and s.count('М')==1 \
       and s.count('А')==2 and s.count('Р')==1 and s.count('Т')==1:
        k+=1
print(k)
