for n in range(9,1000):
    b=bin(n)[2:]
    s=str(b)
    n1=int(s[-2])
    n2=int(s[-1])
    res=n1*n2
    s+=str(res)
    n1 = int(s[1])
    n2 = int(s[0])
    res = n1 * n2
    s += str(res)

    r=int(s,2)
    if r>55:
        print(n)
        break
