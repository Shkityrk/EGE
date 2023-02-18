for x in range(0,15):
    for y in range(0, 17):
        a='123'+str(x)+'5'
        b='67'+str(y)+'9'
        r=int(a,15)+int(b,17)

        if r%131==0:print(y, r//131)