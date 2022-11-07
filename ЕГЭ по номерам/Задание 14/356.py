for x in range(0,17):
    s1='131'+str(x)+'1'
    s2='13'+str(x)+'3'
    if (int(s1,15)+int(s2,17))%11==0:
        print((int(s1,15)+int(s2,17))//11)
