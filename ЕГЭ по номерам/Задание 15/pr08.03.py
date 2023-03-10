for a in range(1,1000):
    if all((((x%250==0)<=(x%10!=0)) or (3*x+2*a>=1000))==1 for x in range(10000)):
        print(a)
        break