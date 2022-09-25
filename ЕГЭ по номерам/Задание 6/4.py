from turtle import *
screensize(5000,5000)
r=70
tracer(0)

for i in range(10):
    rt(60)
    fd(10*r)
    rt(60)


up()
goto(0,0)
dot (5,'black')
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x*r,y*r)
        dot(4,'red')
update()
exitonclick()