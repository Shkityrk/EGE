from turtle import *

screensize(100000, 100000)
k = 50
tracer(0)

for i in range(7):
    goto(xcor() -6 * k, ycor() +9 * k)
    goto(xcor() +6 * k, ycor() -2 * k)
    goto(xcor() -3 * k, ycor() -6 * k)



up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(4, "black")
update()
exitonclick()
