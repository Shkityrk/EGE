from itertools import *
k=0
for x in product('КАПН',repeat=6):
    s=''.join(x)
    if s.count('К')==2 and s.count('А')==2 and s.count('П')==1 and s.count('Н')==1 and \
        'КК' not in s and 'АА' not in s:k+=1
print(k)
