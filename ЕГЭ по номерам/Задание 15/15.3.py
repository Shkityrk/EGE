for a in range (1, 10000):
    flag=0
    for x in range (1, 1000):
        for y in range (1, 1000):
            if ( (5*y+7*x!=129) or (6*x>a) or (8*y>a) )==0:
                flag =1
                break
        if flag ==1:
            break
    if flag==0:
        print (a)