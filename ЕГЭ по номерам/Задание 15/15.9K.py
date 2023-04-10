from itertools import *
b=[''.join(i) for i in product('01',repeat=8)]
a=set()
p={i for i in b if i[0]+i[1]=='11'}
q={i for i in b if i[-1]=='0'}

def f(x):
    A=x in a
    P=x in p
    Q=x in q
    return (not A)<=((P) or (not Q))
for x in b:
    if f(x)==0:a.add(x)
print(len(a))