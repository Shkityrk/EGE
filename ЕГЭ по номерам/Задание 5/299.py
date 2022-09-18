mn=1000
for n in range(1,1000):
    b=bin(n)[2:]
    if b.count('1')%2==0: b=b[1:]
    else: b='1'+b+'00'
    if b.count('1')%2==0: b=b[1:]
    else: b='1'+b+'00'

    r=int(b,2)
    if r>100 :
        if n<mn: mn=n
print(mn)


