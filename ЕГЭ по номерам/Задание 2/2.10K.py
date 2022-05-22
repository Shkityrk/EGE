print('x,y,z,F')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            #for w in 0,1:
                f=not(x==(y<=z))
                if f==0:
                    print(x,y,z,'0')
                else:print(x,y,z,'1')
