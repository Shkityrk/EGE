for i in range(1,100):
    b=bin(i)[2:]

    if b.count('1')%2==0: b+='0'
    else: b+='1'

    r=int(b,2)
    if r>184:
        print(i)
