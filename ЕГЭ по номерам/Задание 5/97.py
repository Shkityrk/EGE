for n in range(1,1000):
    b=bin(n)[2:]
    b+='0' if b.count('1')%2==0 else '1'
    b += '0' if b.count('1') % 2 == 0 else '1'

    r=int(b,2)
    if r>180:
        print(r)
        break
