for a in range(1,50):
    for x in range(1,50):
        for y in range(1,50):
            f=(x*y<a) or (x<y) or (x>=12)
            if f==1:
                print (a)
                break