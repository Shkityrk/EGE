from itertools import product
k=0
for x in product('КОР', repeat=5):
    s=''.join(x)
    k+=1
    if k==182:
        print(s)
        break