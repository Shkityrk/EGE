for x in range(2,1000):
    s=36**17-6**x+71
    c=0
    while s!=0:
        c+=s%6
        s//=6
    if c==61:
        print(x)
        break