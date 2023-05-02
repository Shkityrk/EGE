from turtle import *

screensize(10000,10000)
tracer(0)
r=20

for i in range(5):
    goto(xcor()+6*r,ycor()+8*r)
    goto(xcor() - 8 * r, ycor() +4 * r)
    goto(xcor() +2 * r, ycor() -12 * r)
up()

for x in range(-400,400,r):
    for y in range(-400, 400, r):
        goto(x,y)
        dot(3,'red')
exitonclick()
