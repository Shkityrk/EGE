for n in range(1,101):
    b=bin(n)[2:]
    b=b[::-1]
    r=int(b,2)
    if r==13:
        print(n)