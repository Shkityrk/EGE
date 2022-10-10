from itertools import product
k=0
for x in product('АРСЕНИЙ', repeat=4):
    s=''.join(x)
    if s[0]!='Й' and ('А' in s or 'Е' in s or 'И' in s):
        k+=1
        print(s)
print(k)