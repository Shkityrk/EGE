from turtle import *
tracer(0)
screensize(3000,3000)
k=15

for i in range(10):
    for n in range(3):
        fd(10*k)
        rt(90)
        fd (10 * k)
        rt(270)
    rt(90)
up()
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(3, "blue")
update()
exitonclick()