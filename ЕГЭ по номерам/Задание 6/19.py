from turtle import *
screensize(10000,10000)
tracer(0)
r=60

fd(9*r)
rt(90)
for i in range(2):
    fd(3 * r)
    rt(90)
    fd(3 * r)
    rt(270)

for i in range(2):
    fd(3*r)
    rt(90)
fd(9*r)


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