from itertools import product
k=0
for x in product('ВОРН', repeat=5):
    s=''.join(x)
    if not 'ОО' in s and s.count('В')==1 and s.count('Н')==1\
       and s.count('О')==2 and s.count('Р')==1:
        k+=1
print(k)
