from itertools import product
k=0
for x in product('ЕСАУЛ', repeat=5):
    s=''.join(x)
    if not 'ЕУ' in s and not 'ЕА' in s and not 'АЕ' in s \
       and not 'АУ' in s and not 'УЕ' in s and not 'УА' in s \
       and s.count('Е')==1 and s.count('С')==1 \
       and s.count('А')==1 and s.count('У')==1 and s.count('Л')==1 :
        k+=1
print(k)
