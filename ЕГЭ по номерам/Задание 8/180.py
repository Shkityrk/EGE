from itertools import product
k=0
for x in product('МЕЧТА', repeat=6):
    s = ''.join(x)
    if s.count('А')>=3:
        k+=1
print(k)