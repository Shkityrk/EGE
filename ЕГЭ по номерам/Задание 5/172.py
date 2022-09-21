for n in range(1,110):
    b=bin(n)[2:]
    while len(b)%4!=0:
        b='0'+b
    b=b[0]+b[1]+b[-2]+b[-1]

    r=int(b,2)
    if r==7:
        print(n)