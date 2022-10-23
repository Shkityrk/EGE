for x in range(0,100):
    s1='55'+str(x)+'36'
    s2=str(x)+'2724'
    n=int(s1,19)+int(s2,19)
    if n%11==0:
        print(n//11)
        break