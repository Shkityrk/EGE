from itertools import permutations
k=0

for x in permutations('РУЛЬКА'):
    s=''.join(x)
    if s[0]!='Ь' and ('УЬ' not in s) and ('АЬ' not in s):
        k+=1
print(k)
