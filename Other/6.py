from turtle import *

screensize(10000,10000)
tracer(0)
r=50

for _ in range(6):
    rt(120)
    fd(6*r)
up()

for x in range(-300,300,r):
    for y in range(-300, 300, r):
        goto(x,y)
        dot(3,'red')
exitonclick()