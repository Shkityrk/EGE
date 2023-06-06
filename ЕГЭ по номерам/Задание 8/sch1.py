from itertools import *
k=0
for x in product('ЕКОФ', repeat=5):
    s=''.join(x)
    k+=1
    if s=='ФЕФКО':
        print(k,s)
        break