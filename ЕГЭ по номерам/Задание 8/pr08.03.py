from itertools import product
k=0

for x in product('СПОРТЛ', repeat=9):
    s=''.join(x)
    if s.count('С')==1 and s.count('П')==1 and s.count('О')==3 and s.count('Р')==1 and s.count('Т')==2 and s.count('Л')==1 and  s[0]!=s[-1]:k+=1
print(k)