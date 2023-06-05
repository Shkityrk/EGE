from itertools import *
k=0
for x in product('УСЛОВИЕ',repeat=7):
    s=''.join(x)
    if s[0]!='И' and s[-1]!='О':
        s=s.replace('С','*').replace('Л','*').replace('В','*')
        if s.count('**')==0:k+=1
print(k)