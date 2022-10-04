from itertools import permutations
k=0
for x in permutations('АЙСБЕРГ'):
    s=''.join(x)
    if s[0]!='Й' and all(n not in s for n in ['ЙА','ЙЕ']):
        k+=1
print(k)