for x in range (1,1000,1):
    a=125**7-68**4+x
    c1=0
    c3=0
    c4=0
    while a!=0:
        if a%5 ==1:
            c1=c1+1
        if a%5 ==3:
            c3=c3+1
        if a%5 ==4:
            c4=c4+1
        a=a//5
    if c1==2 and c3==1 and c4==14:
        print (x)
        break