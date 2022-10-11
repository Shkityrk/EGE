from itertools import product
k=0
for x in product('ЛОДКА', repeat=4):
    s=''.join(x)
    if s.count('О')>=2:k+=1
print(k)