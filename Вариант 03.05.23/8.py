from itertools import *
k=0
for x in product('ИКЛНОР', repeat=4):
    s=''.join(x)
    k+=1
    print(k,s)
    if s=='КИНО':
        break