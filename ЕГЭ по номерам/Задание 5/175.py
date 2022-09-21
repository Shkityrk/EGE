for n in range(20,50):
    b=bin(n)[2:]
    print(b)
    b=b.replace(b[-1],"",1)
    b=b.replace(b[-1],"",1)
    r=int(b,2)
    print(n,b)

    print("")

