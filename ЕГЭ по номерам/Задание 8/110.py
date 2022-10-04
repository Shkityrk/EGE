from itertools import permutations
k=0

for x in permutations('РУЛЬКА'):
    s=''.join(x)
    if s[0]!='Ь' and all(m not in s for m in ['УЬ','АЬ']):
        k+=1
print(k)