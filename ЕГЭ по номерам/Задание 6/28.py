from turtle import *
screensize(10000,10000)
tracer(0)
r=60


for i in range(5):
    fd(8*r)
    rt(120)
    for j in range(2):
        fd(4*r)
        rt(60)
    fd(4*r)
    rt(120)


up()
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x*r,y*r)
        dot(4,"red")
for x in range(-100,100):
    for y in range(-100, 100):
        if x==0 or y==0:
            goto(x*r,y*r)
            dot(4,"black")
update()
exitonclick()