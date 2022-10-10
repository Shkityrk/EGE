from itertools import permutations
k=0
for x in permutations('АПОРТ'):
    s=''.join(x)
    k+=1
    if 'АО' in s or 'ОА' in s:
        k-=1
print(k)
