for x in range(0,15):
    a='135'+str(x)+'7'
    b='7'+str(x)+'531'
    r=int(a,15)+int(b,15)
    if r%14==0:
        print(r//14)
        break