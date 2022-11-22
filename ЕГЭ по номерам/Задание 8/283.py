from itertools import product
k=0

for x in product('АНТИУОПЯ', repeat=16):
    s=''.join(x)
    if s.count('АНТИУТОПИЯ')>0:
        k+=1
        print(k,s)
