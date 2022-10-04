from itertools import permutations

k=0
for x in permutations('НИГРОЛ'):
    s=''.join(x)
    if s[0]!='О' and not 'ОИГ' in s:
        k+=1
print(k)