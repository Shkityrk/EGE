from turtle import *
tracer(0)
screensize(10000,10000)

r=20
down()
for _ in range(7):
    fd(10*r)
    rt(120)
up()

for x in range(-200,200,r):
    for y in range(-200, 200, r):
        goto(x,y)
        dot(3,'red')
exitonclick()