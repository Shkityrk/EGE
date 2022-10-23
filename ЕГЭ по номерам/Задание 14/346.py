for x in range(0,10):
    s1='123'+str(x)+'5'
    s2='1'+str(x)+'233'
    n=int(s1,15)+int(s2,15)
    if n%14==0:
        print(n//14)

