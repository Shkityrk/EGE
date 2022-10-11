from itertools import product
k=0
for x in product('КРЕСЛО', repeat=4):
    s=''.join(x)
    if s[0] in ['К','Р','С','Л'] and s[-1] in ['Е','О']:
        k+=1
print(k)