print('x,y,z,w')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0,1:
                f=((w<=y) or (not(y<=z))) and (not x) and (not (x==z))
                if f==1:
                    print(x,y,z,w)