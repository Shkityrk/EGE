from itertools import product
k=0
for x in product('ABCD', repeat=4):
    s=''.join(x)
    if s[0]!= 'A' and s[1]!=s[2]:
        k+=1
print(k)
