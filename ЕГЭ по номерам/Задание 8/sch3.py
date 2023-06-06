from itertools import *
k=0
for x in product('БОГИНЯ', repeat=6):
    s=''.join(x)
    if s.count('О')==2:
        k+=1
print(k)