from itertools import *
k=0
for x in product('КАТЕР', repeat=6):
    s=''.join(x)
    if s[0]!='Т' and s[1]!='Т' and 'КТ' not in s and s.count('Т')<=1:
        k+=1
print(k)