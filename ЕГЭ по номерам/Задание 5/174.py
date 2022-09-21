for n in range(10,2501):
    b=bin(n)[2:]
    while '0' in b:
        b=b.replace('0',"",1)

    r=int(b,2)
