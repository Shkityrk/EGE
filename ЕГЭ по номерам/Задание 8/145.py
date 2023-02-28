from itertools import product
k=0
for x in product('РАДУГ', repeat=6):
    s=''.join(x)
    if (s.count('Р')+ s.count('Д')+ s.count('Г'))>=3:
        k+=1
print(k)
