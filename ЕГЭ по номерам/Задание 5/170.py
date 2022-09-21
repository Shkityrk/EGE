for n in range(1000,100000):
    b=bin(n)[2:]
    b=b[::-1]
    

    r=int(b,2)
    if r==29:
        print(n)