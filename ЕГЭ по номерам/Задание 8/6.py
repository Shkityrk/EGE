from itertools import product
k=0
for x in product('АКРУ', repeat=5):
    k+=1
    s=''.join(x)
    if k==250:
        print(s)
        break