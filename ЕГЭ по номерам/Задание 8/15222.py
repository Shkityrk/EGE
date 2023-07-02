from itertools import *
chet='0246'
nech='1357'
k=0
for x in product('01234567', repeat=5):
    s=''.join(x)
    num=s
    if '1' not in s and s[0]!='0' and all(s.count(t)<=1 for t in '01234567'):
        for f in chet:
            s=s.replace(f,'Ч')
        for f in nech:
            s=s.replace(f,'Н')
        if not 'ЧЧ' in s and not 'НН' in s:
            k+=1
            print(num,s)

print(k)