from itertools import *
k=0
for x in product('АПРЕЛ', repeat=6):
    s=''.join(x)
    s=s.replace('А','*').replace('Е','*').replace('П','/').replace('Р','/').replace('Л','/')
    if s.count('*')>s.count('/'):
        k+=1
print(k)