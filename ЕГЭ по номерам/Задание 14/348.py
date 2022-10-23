for i in range(0,19):
    s1='9009'+str(i)
    s2='2257'+str(i)
    n=int(s1,18)+int(s2,18)
    if n%15==0:
        print(i,n//15)

