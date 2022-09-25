from turtle import *
screensize(1000,1000)
r=40
tracer(0)

for i in range(15):
    fd(4*r)
    rt(60)


up()

for x in range(-100,100):
    for y in range(-100, 100):
        if x==0 or y==0:
            goto(x*r,y*r)
            dot(4,'black')
        elif x>0 and y>0:
            goto(x*r,y*r)
            dot(4,'red')
goto(0,0)
dot (5,'black')
goto(1,1)
dot (5,'black')
update()
exitonclick()