print('x,y,z,w')
k=0,1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                f=(y<=z) and (not (z and x))
                if f==1:
                    print(x,y,z)