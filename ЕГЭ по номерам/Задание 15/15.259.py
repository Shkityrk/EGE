for a in range(1,1000):
    f=1
    for x in range(1,100):
        for y in range(1,100):
            f*=((x<a) and (x*x>=120)) or ((y*y<=20) and (y>a))
    if f ==1:
        print(a)