from itertools import product
k=0
for x in product('01234', repeat=6):
    s=''.join(x)
    if s[0] not in '01' and s[-1] not in '34':
        k+=1
        print(s)
print(k)