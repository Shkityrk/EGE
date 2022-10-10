from itertools import product
k=0
for x in product('012345678', repeat=5):
    s=''.join(x)
    if s[0] in ['2','4','6','8'] and s[-1] in['2','3','4','5','6','7','0'] and \
       s.count('3')<=1:
        k+=1
print(k)
