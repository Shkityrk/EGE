from itertools import *
k=0
l='КАМЫШ'
for x in product(l, repeat=7):
    s=''.join(x)
    if s[0]!='А' and s[0]!='Ы':
        if 'КК' not in s and 'ММ' not in s and 'ЫЫ' not in s and'ШШ' not in s and 'АА' not in s:
            k+=1

print(k)