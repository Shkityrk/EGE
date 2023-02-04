from itertools import *
k=0
for x in product('РУСЛАН', repeat=5):
    n=0
    for i in range(len(x)):
        if x[i] in 'УА':n+=1
    if n<=1:
        k+=1
        print(x)

print(k)