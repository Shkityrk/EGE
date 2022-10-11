from itertools import product
k=0
for x in product('123AB', repeat=8):
    s=''.join(x)
    if s.count('A')+s.count('B')==2:
        k+=1
print(k)