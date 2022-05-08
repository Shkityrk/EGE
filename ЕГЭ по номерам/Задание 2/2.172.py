print('x,y,z,w')
k=0,1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                f=((not x) or y or (not z)) and (x or (not y)) or (not w)
                if f==0:
                    print(x,y,z,w)