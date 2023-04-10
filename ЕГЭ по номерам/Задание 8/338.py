from itertools import *
k=0

for x in product('012345678',repeat=10):
    s=''.join(x)
    f=1
    if s[0]!='0':
        for i in '012345678':
            if s.count(i)>2:f=0
        if f==1:k+=1
print(k)