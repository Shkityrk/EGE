for x in range(0,17):
    a='135'+str(x)+'9'
    b='9'+str(x)+'531'
    r=int(a,17)+int(b,17)
    if r%9==0:
        print(r//9)
