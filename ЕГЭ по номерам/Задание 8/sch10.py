from itertools import *
k=0
for n in range(3,7):
    for x in product('РАСЧЕК',repeat=n):
        k+=1
print(k)