for x in range(21):
    for y in range(21):
        a=21**4+2*21**3+y*21**2+x*21+9+3*21**4+6*21**3+y*21**2+9*21+9
        if a%18==0:
            print(x,y,a//18)