from turtle import *
screensize(10000,10000)
tracer(0)
r=60
for i in range(10):
    goto(xcor()+3*r,ycor()+6*r)
    goto(xcor() +7 * r, ycor() -2 * r)
    goto(xcor() -10 * r, ycor() -4 * r)


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