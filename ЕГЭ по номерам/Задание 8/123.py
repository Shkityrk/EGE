from itertools import product
k=0
for x in product('АСИН', repeat=7):
    s=''.join(x)
    if s.count('А')==2 and s.count('С')==3 and s.count('И')==1\
       and s.count('Н')==1:
        k+=1
print(k)
