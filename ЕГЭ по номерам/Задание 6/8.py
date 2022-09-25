from turtle import *

screensize(100000, 100000)
k = 50
tracer(0)
left(90)
for i in range(15):
    goto(xcor() + 10 * k, ycor() + 10 * k)
    goto(xcor() + 3 * k, ycor() -6 * k)
    goto(xcor() -9 * k, ycor() +3 * k)



up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(4, "black")
update()
exitonclick()
