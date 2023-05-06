from turtle import *

screensize(10000,10000)
tracer(0)
r=15

for i in range(2):
    fd(5*r)
    rt(90)
    fd(15*r)
    rt(90)
up()
bk(7*r)
rt(90)
fd(12*r)
lt(90)
down()
for i in range(2):
    fd(65*r)
    rt(90)
    fd(120*r)
    rt(90)

up()
for x in range(-300,300,r):
    for y in range(-300, 300, r):
        goto(x,y)
        dot(3,'red')
exitonclick()