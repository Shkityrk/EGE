from itertools import product
k=0
for x in product('АОУ', repeat=5):
    k+=1
    s=''.join(x)
    if k==210:
        print(s)