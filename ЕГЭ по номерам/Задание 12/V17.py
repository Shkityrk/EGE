r=[]
mn=10**10
for n in range(1,1000):
    x='>'+'0'*15+'1'*n+'2'*15
    while '>0' in x or '>1' in x or '>2' in x:
        if '>0' in x:
            x=x.replace('>0','22>',1)
        if '>1' in x:
            x = x.replace('>1', '2>', 1)
        else:
            x = x.replace('>2', '1>', 1)
    s=0
    s= x.count('1')+x.count('2')*2
    if 2**(s-1)%s==1:
        print(n)
        break
print(mn)
