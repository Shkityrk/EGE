from turtle import *
screensize(1000,1000)
r=20
tracer(0)

for i in range(15):
    fd(15*r)
    rt(120)


up()
goto(0,0)
dot (5,'black')
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x*r,y*r)
        dot(4,'red')
update()
exitonclick()