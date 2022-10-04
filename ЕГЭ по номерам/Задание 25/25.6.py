b=[]
for c1 in '0123456789abcdef':
    for c2 in '0123456789abcdef':
        a=int(f'1{c1}ded{c2}ced',16)
        if a%121==0:
            b+=[(a,a//121)]
for x in b[::-1]:
    print(*x)