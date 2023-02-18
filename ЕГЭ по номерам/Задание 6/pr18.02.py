from turtle import *
tracer(0)
screensize(10000,10000)

r=20
for i in range(15):
    goto(xcor() + 10 * r, ycor() + 10 * r)
    goto(xcor() + 3 * r, ycor() -6 * r)
    goto(xcor() -9 * r, ycor() + 3 * r)
up()
for x in range(-200,700,r):
    for y in range(-200,700,r):
        goto(x,y)
        dot(3,'red')
exitonclick()