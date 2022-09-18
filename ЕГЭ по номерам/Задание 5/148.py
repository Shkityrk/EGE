for n in range(1,100):
    b = bin(n)[2:]
    b = b + b[-1]
    b+='0' if bin(n)[2:].count('1')%2==0 else '1'
    b+='0' if b.count('1')%2==0 else '1'
    r=int(b,2)
    if r>90:
        print(n)
        break

