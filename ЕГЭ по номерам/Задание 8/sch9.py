from itertools import *
k=0
for x in product('КРУЖА',repeat=7):
    s=''.join(x)
    s=s.replace('У','*').replace('А','*')
    if s.count('*')==2:k+=1
print(k)