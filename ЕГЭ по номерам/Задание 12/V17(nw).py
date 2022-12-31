from itertools import permutations

def is_prost(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return 0
    else: return 1

for n in range(1,1000):
    a='0'*15
    b='1'*n
    c='2'*15
    for z in permutations([a,b,c]):
        x=str(z)
        x='>'+x
        while '>0' in x or '>1' in x or '>2' in x:
            if '>0' in x:
                x=x.replace('>0','22>',1)
            if '>1' in x:
                x = x.replace('>1', '2>', 1)
            else:
                x = x.replace('>2', '1>', 1)
        s=x.count('1')+x.count('2')*2
        if is_prost(s):
            print(n)
            break