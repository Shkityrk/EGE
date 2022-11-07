from turtle import *

##нахождение кол-ва сторон фигуры, либо задать сразу
##n=
a=int(input("Сумма углов внутри цикла="))
if a==180: n=2
else:n=int(360/(180-a) if 360%(180-a)==0 else 0)

color('black', 'red')
speed(1000)
r=100

begin_fill()
rt(45)#угол отклонения фигуры
for i in range(n):
    fd(20*r)
    right(90)
    fd(30*r)
    right(90)
end_fill()

canvas = getcanvas()
k = 0
for x in range(-100,100):
    for y in range(-100,100):
        item = canvas.find_overlapping(x*r, y*r, x*r ,y*r)
        if len(item)==1 and item[0] == 5:
            k += 1
print(k)
exitonclick()