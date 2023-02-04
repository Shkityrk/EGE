for x in range(0,17):
    a=17**3+x*17
    b=15*17**4+x*17**2+15*17+15
    if (a+b)%13==0:print(x, (a+b)/13)