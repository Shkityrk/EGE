from turtle import *
screensize(10000,10000)
r=20
tracer(0)

for i in range(7):
    fd(20*r)
    rt(240)
    fd(10*r)
    rt(240)

    fd(20 * r)
    rt(120)
    fd(10 * r)
    rt(120)

up()

for x in range(-400,400,r):
    for y in range(-400,400,r):
        goto(x,y)
        dot(3,'red')
exitonclick()