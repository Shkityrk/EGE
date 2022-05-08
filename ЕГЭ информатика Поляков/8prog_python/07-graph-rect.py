# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 7. Рисование прямоугольников и окружностей
#

from graph import *

penColor("red")
line(10, 20, 60, 20)
line(60, 20, 60, 50)
line(60, 50, 10, 50)
line(10, 50, 10, 20)

polygon( [(110,20), (160,20), (160,50), (110,50), (110,20)] )

penColor("blue")       # цвет границы
brushColor("yellow")   # цвет заливки
rectangle(10, 120, 60, 150)

penColor("red")
brushColor("green")
circle(200, 150, 50)

run()


