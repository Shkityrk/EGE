from itertools import *
k=0
for x in product('РУСЛАН', repeat=5):
    s="".join(x)
    if s.count('У')<=1 and s.count('А')<=1:k+=1

print(k)