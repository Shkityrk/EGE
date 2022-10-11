from itertools import product
k=0
for x in product('МИКРЯ', repeat=8):
    s=''.join(x)
    if s.count('М')==2 and s.count('И')==3 and s.count('К')==1 \
            and s.count('Р')==1 and s.count('Я')==1:
        k+=1
print(k)

