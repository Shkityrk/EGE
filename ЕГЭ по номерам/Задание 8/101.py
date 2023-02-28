from itertools import permutations
k=0
for x in permutations('ШАНЕЛЬ'):
    s=''.join(x)
    if s[0]!='Ь' and not 'ЕАЬ' in s:
        k+=1

print(k)
