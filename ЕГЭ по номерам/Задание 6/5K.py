from turtle import *
screensize(10000,10000)
color=("black","red")
tracer(0)

r=20

for _ in range(14):
    for x in range(3):
        fd(3*r)
        rt(90)
    rt(180)
up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*r,y*r)
        dot(4,"red")
exitonclick()