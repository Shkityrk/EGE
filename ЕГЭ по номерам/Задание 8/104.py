from itertools import permutations
k=0
for x in permutations('НАДПИСЬ'):
    s=''.join(x)
    if s[0]!='Ь' and not 'ЬИА' in s:
        k+=1
print(k)