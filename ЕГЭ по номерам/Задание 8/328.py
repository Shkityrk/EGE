from itertools import *
k=0
for x in product('СВЯТОЛА',repeat=7):
    s=''.join(x)
    r=0
    for i in range(len(s)):
        if s[i] in 'ЯОА':r+=1
        else:r-=1
    if r>0:k+=1
print(k)