a=[int(x**2) for x in range(1,1000)]
for n in range(1,1000):
    s='>'+'1'*n+'0'*15+'2'*15
    while '>0' in s or '>1' in s or '>2' in s:
        if '>0' in s:s=s.replace('>0','22>',1)
        if '>1' in s: s = s.replace('>1', '2>',1)
        if '>2' in s: s = s.replace('>2', '1>', 1)
    r=s.count('1')+s.count('2')*2
    if r in a:
        print(n)
        break