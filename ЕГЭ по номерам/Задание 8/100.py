from itertools import permutations
k=0
for x in permutations('ПАНЕЛЬ'):
    s=''.join(x)
    if s[0]!='Ь' and not 'ЕАП' in s:
        k+=1

print(k)