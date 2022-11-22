from itertools import product
k=0
for x in product ('ШТСМКИЕВА',repeat=5):
    k+=1
    if (x[0]==x[-1]) and (x[1]==x[-2]) and (x[0] in 'ИЕА') and (x[1] in 'ИЕА') and (x[2] in 'ШТСМКВ'):
        print(k,x)