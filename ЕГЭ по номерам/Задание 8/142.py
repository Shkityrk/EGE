from itertools import product
k=0
for x in product('ВАЯЮЩИЙ', repeat=4):
    s=''.join(x)
    if s[0]!='Й' and  (s.count('А')>0 or s.count('Я')>0 \
       or s.count('Ю')>0 or s.count('И')>0) :
        k+=1
print(k)
