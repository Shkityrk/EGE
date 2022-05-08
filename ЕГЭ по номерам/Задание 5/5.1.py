def step(x1,y1, rng):
    for _ in range (rng):
        x1+=1
        y1-=1
        x1 += 1
        y1+=1
        x1-=1
        y1 += 1
        y1 += 1
        x1-=1
    return (x1,y1)



for i in range(1,1000000):
    x, y = 0, 0
    x2,y2=step(x,y,i)
    if x2==0 and y2==0:
        print(i)
        break
