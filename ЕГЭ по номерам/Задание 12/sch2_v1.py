a=[int(x**2) for x in range(1,1000)]
for n in range(101,1000):
    s='0'+'1'*(n-50)+'21'*50+'0'
    while '00' not in s:
        s=s.replace('02','101',1)
        s = s.replace('11', '2', 1)
        s = s.replace('012', '30', 1)
        s = s.replace('010', '00', 1)
    r=s.count('1')+s.count('2')*2
    if r in a:
        print(n)
        break