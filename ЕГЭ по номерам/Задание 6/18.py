from turtle import *
screensize(10000,10000)
tracer(0)
r=60

rt(30)
for i in range(30):
    rt(30)
    fd(3 * r)
    rt(30)

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