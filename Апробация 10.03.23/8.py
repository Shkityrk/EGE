from itertools import product
k=0
for x in product('АЙКОС', repeat=5):
    k+=1
    s=''.join(x)
    if s.count('О')<=1 and 'СС' not in s:
        print(k,s)