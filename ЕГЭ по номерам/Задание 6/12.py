from turtle import *

screensize(100000, 100000)
k = 20
lt(90)
tracer(0)
fd(200*k)
for i in range(200):
    rt(90)
    fd(50*k)




up()
for x in range(-100, 100):
    for y in range(90, 400):
        goto(x * k, y * k)
        dot(4, "black")
update()
exitonclick()
