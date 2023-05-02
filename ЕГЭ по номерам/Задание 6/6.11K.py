from turtle import *

screensize(10000,10000)
tracer(0)
r=20

for i in range(7):
    goto(xcor()+6*r,ycor()-9*r)
    goto(xcor() - 6 * r, ycor() +2 * r)
    goto(xcor() + 12 * r, ycor() +3 * r)
up()

for x in range(-400,400,r):
    for y in range(-400, 400, r):
        goto(x,y)
        dot(3,'red')
exitonclick()