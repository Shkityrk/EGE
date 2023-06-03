f=open('27-38a.txt')
from itertools import *
n=int(f.readline())
a=[str(x)[:-1] for x in f.readlines()]
for i in range(n):
    for j in range(i+1,n):
        l=a[i:j]
        m=''.join(l)
        if m.count('5')>=2:
            m=m.replace('5','',1).replace('5','',1)
            m='5'+m+'5'
            print(m)