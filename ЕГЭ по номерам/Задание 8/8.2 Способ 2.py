from itertools import product
a=list(product(('САЛО'),repeat=5))
c=0
for t in a:
    if t.count('С')==1:
        c+=1
print (c)