for a in range(1,2000):
    for x in range(0,16):
        for y in range(0, 16):
            m='2'+str(y)+'23'+str(y)+'5'
            n='67'+str(x)+'9'+str(y)
            if (int(m,15)+a)%(int(n,13))==0:
                print(a,x,y)

