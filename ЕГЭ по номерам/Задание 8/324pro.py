from itertools import *
n=0
for x in product('nh', repeat=10):
    s=''.join(x)
    if s.count('n')==3 and 'nn' not in s:
        if s[0]=='h':n+=3*4**9
        else:n+=4**10
print(n)