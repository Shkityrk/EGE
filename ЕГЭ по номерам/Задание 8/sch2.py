from itertools import *
k=0
for x in product('ГОЭ', repeat=5):
    s=''.join(x)
    k+=1
    if k==78:
        print(k,s)
        break