from turtle import *
screensize(10000,10000)
tracer(0)
r=60
lt(90)

for i in range(11):
    fd(4*r)
    rt(60)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        if x==0 or y==0:
            goto(x * r, y * r)
            dot(4, "black")
        else:
            goto(x*r,y*r)
            dot(4,"red")


update()

exitonclick()