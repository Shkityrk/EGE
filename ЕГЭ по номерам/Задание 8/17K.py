from itertools import product
k=0
for x in product('ЕЛМРУ',repeat=4):
    k+=1
    print(k,*x)