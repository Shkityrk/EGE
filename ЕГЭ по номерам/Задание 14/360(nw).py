for a in range(1,2000):
    for x in range(0,15):
        for y in range(0, 15):
            m=2*15**5+y*15**4+2*15**3+3*15**2+x*15+5
            if (x<13) and (y<13):
                n=6*13**4+7*13**3+x*13**2+9*13+y
            if (m+a)%n==0:
                print(a)
                break

