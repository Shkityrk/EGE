from itertools import *
k=0
for x in product('ГРОЗА', repeat=7):
    s=''.join(x)
    if s.count('З')>=2:
        k+=1
print(k)