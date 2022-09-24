for n in range(1,1000):
    b=bin(n)[2:]
    b+='01' if b.count('1')%2==0 else '10'

    r=int(b,2)
    if r>81:
        print(r)
        break