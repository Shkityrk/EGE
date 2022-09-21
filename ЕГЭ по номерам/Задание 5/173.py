for n in range(100,1,-1):
    b=bin(n)[2:]
    while len(b)%4!=0:
        b='0'+b
    b=b[:-1]
    b=b[::-1]
    

    if n==int(b,2):
        print(n)
        break


