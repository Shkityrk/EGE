import turtle
from turtle import *
screensize(1000,1000)
r=15
tracer(0)

for i in range(10):
    fd(6*r)
    rt(120)

up()
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x*r,y*r)
        dot(4,'red')
exitonclick()