print('a,b,c')
for a in range(2):
    for b in range(2):
        for c in range(2):
            if (a and (not c)) or ((not b) and (not c))==1:
                print(a,b,c,1)
            else: print(a,b,c,0)