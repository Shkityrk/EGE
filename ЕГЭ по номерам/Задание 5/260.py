mn=100000
for n in range(1,1000):
    b=bin(n)[2:]
    if b[-1]!='0':
        pass
    else:
        b=b.replace(b[-1], b[0]+b[1])

        b=b[::-1]
    r=int(b,2)
    if r==123:
       print(n)

