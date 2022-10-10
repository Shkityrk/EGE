from itertools import product
k=0
for x in product('ТРА', repeat=7):
    s=''.join(x)
    if s.count('А')==3 and s.count('Т')==3 and s.count('Р')==1:
        k+=1
print(k)
