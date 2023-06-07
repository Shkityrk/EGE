from turtle import *
screensize(10000,10000)
r=20
tracer(0)
for _ in range(20):
    goto(xcor()+4*r,ycor()+3*r)
    goto(xcor() -4*r, ycor() -3*r)
    goto(xcor() -12*r, ycor() -5*r)
    goto(xcor()+12*r, ycor() + 5*r)

up()
for x in range(-300,300,r):
    for y in range(-300, 300, r):
        goto(x,y)
        dot(3,'red')
exitonclick()