from itertools import permutations
k=0
for x in permutations('ИГРОК'):
    s=''.join(x)
    if s[0]!='К' and not 'РОК' in s: k+=1
print(k)