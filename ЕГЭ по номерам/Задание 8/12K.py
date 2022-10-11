from itertools import product
k=0
for x in product('ГЕПАРД', repeat=5):
    s=''.join(x)
    if s.count('Г')==1 and s[0]!='А' and s[-1]!='Е':
        k+=1
print(k)