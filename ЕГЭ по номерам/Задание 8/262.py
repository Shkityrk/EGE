from itertools import product

a=['16', '36','56','76','61','63', '65','67']
k=0
for x in product('01234567',repeat=5):
    s=''.join(x)
    if s[0]!='0' and s.count('6')==1 and all(i not in s for i in a):

        k+=1
print('total', k)