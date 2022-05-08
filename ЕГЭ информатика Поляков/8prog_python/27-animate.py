# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 27. Анимация
#

from graph import *

def update():
  global xCenter   # будем изменять xCenter
  xCenter += 5     # новая x-координата центра
  moveObjectBy(obj, 5, 0)
  if xCenter >= 400-R:
    close()

def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()

brushColor("blue")
rectangle(0, 0, 400, 400)

R = 10
xCenter = 10
yCenter = 200
penColor("yellow")
brushColor("yellow")
obj = circle(xCenter, yCenter, R)

onTimer(update, 10)
onKey(keyPressed)

run()