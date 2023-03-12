from turtle import *
tracer(0)
screensize(10000,10000)
rt(90)
r=20
for _ in range(4):
    fd(10*r)
    rt(270)
up()
fd(3*r)
rt(270)
fd(5*r)
rt(90)
down()
for _ in range(2):
    fd(10*r)
    rt(270)
    fd(12*r)
    rt(270)
up()

for x in range(-500,500,r):
    for y in range(-500, 500, r):
        goto(x,y)
        dot(3,'red')

exitonclick()