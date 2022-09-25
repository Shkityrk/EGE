import turtle
turtle.screensize(10000,10000)
k=50
turtle.tracer(0)

for i in range(8):
    turtle.fd(12*k)
    turtle.rt(90)

turtle.up()
for x in range(-100,100):
    for y in range(-100, 100):
        turtle.goto(x*k,y*k)
        turtle.dot(4,"black")
turtle.update()
turtle.exitonclick()
    