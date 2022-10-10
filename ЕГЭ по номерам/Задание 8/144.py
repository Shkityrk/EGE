from itertools import product
k=0
for x in product('АЗИМУТ', repeat=6):
    s=''.join(x)
    if (s.count('З')+ s.count('М')+s.count('Т'))>=3:
        k+=1
print(k)