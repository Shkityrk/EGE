for x in range(0,21):
    a=10*21**5 + 11*21**4 + 12*21**3 + 1*21**2 +x*21
    b=13*21**3 + x*21**2 +9*21+8

    if (a+b)%65==0:print((a+b)//65)