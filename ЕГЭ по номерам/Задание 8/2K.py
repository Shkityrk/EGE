from itertools import product
def f(x):
    if x not in ['W','X','Y','Z'] :
        return 1
    else: return 0
tr=1
k=0
for x in product('ABCWXYZ', repeat=6):
    s=''.join(x)
    if s[0] in ['W','X','Y','Z'] and s[-1] in ['W','X','Y','Z']:
        for i in range(2,6):
            if s[i] in ['W','X','Y','Z'] : tr=0

        if tr==1:
            k+=1
            print(s)
print(k)