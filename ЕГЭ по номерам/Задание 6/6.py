from turtle import *

screensize(10000, 10000)
k = 50
tracer(0)

for i in range(36):
    rt(60)
    fd(1*k)
    rt(60)
    fd(1 * k)
    rt(270)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(4, "black")
update()
exitonclick()
