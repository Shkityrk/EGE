from turtle import *
screensize(10000,10000)
tracer(0)
r=30

lt(90)
for i in range(4):
    for j in range(4):
        for c in range(4):
            fd(3*r)
            rt(120)
        fd(3*r)
    fd(3*r)

update()
exitonclick()