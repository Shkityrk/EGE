from turtle import *
screensize(10000,10000)
r=20
tracer(0)

rt(40)
for _ in range(10):
    fd(15*r)
    rt(60)
    fd(5*r)
    rt(120)

up()
for x in range(-300,300,r):
    for y in range(-300, 300, r):
        goto(x,y)
        dot(3,'red')
exitonclick()