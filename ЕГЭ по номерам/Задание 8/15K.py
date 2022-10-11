from itertools import permutations
k=0
for x in permutations('ВАЙФУ',r=4):
    s=''.join(x)
    if s[0]!='Й' and all(n not in s for n in ['ВФ','ФВ']):
        k+=1
print(k)