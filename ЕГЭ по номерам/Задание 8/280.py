g='aeiouy'
k=0
from itertools  import product
for s in product('abcdefghigklmnopqrstuvwxyz', repeat=5):
    if any(x in s for x in g):k+=1   
            
print(k)
