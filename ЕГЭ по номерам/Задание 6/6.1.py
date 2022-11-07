import turtle
from turtle import *
tracer(0) # убирает анимацию рисования черепашкой рисунка.
screensize(10000,10000)#появятся крутилки для пролистывания вверх, вниз, вперед, назад
r=25 ##масштаб черепашки
color("black", "red")
fd(100*r)
rt(90)
fd(100*r)

begin_fill()
rt(30)

for i in range(4):
    fd(30*r)
    rt(90)
end_fill()
up()# строим сетку
'''for x in range(-10*r,10*r,r):#координата х
    for y in range(-15*r, 10*r,r):# координата у
        goto(x,y)# переводим к точке ьтакой то
        dot (3)# ставим точечку
'''
canvas = getcanvas()
cnt = 0
for y in range(-300*r, 300*r, r):
    for x in range(-300*r, 300*r, r):
        item = canvas.find_overlapping(x, y, x, y)

        if len(item)==1:
            cnt += 1

print(cnt)

update()#обновляем рисунок, т.к. не анимация, а статичный кадр. использовать вместе с tracer(0)
turtle.mainloop()# в пайчарме, после выполнения программы закрывается окно. этот бесконечный цикл предотвращает закрытие программы после выполнения
#exitonclick() или так, или инпут