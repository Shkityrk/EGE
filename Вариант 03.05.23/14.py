for x in range(15,0-1,-1):
    a=1*15**3+x*15**2+5*15+1
    b=3*15**2+x*15+2
    if (a-b)%4==0:
        print(x,a-b,(a-b)//4)