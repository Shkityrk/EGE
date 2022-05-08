# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 9. Рисование с процедурами
#

from graph import *

def frame():
  penColor("black")
  brushColor("green")
  rectangle(100, 100, 200, 200)

def roof():
  penColor("black")
  brushColor("brown")
  polygon([(90,100), (150,50),
           (210,100), (90,100)])

def window():
  penColor("white")
  penSize(3)
  brushColor("black")
  rectangle(120, 120, 150, 170)
  line(120, 140, 150, 140)
  line(135, 140, 135, 170)

frame()
roof()
window()

run()


