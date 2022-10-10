from itertools import product
a=['АА']
k=0
for x in product('КАБЛ', repeat=6):
    s=''.join(x)
    if s.count('А')==3 and s.count('К')==1 and s.count('Б')==1 and s.count('Л')==1 and all(i not in s for i in a):
        k+=1
print(k)