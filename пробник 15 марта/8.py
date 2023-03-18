from itertools import *
k=0

for x in product('POLYGN',repeat=5):
    s=''.join(x)
    if s[0]==s[-1] and s[1]==s[-2] and s[3] in 'OY':k+=1

print(k)