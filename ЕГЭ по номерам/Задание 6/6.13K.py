from turtle import *

screensize(10000,10000)
tracer(0)
r=20

for i in range(3):
    goto(xcor()-3*r,ycor()-4*r)
    goto(xcor() - 12 * r, ycor() - 5 * r)
    goto(xcor() +15 * r, ycor() +8 * r)
    goto(xcor(), ycor() +1 * r)
up()

for x in range(-400,400,r):
    for y in range(-400, 400, r):
        goto(x,y)
        dot(3,'red')
exitonclick()
