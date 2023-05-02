from turtle import *

screensize(10000,10000)
r=20
tracer(0)

x=17

for _ in range(5):
    fd(x*r)
    rt(90)
    fd(3*r)
up()

for x in range(-1000,1000,r):
    for y in range(-1000, 1000, r):
        goto(x,y)
        dot(3,'red')
exitonclick()