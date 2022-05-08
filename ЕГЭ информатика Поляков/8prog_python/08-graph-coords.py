# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 8. Рисование квадрата с вводом координат
#

from graph import *

print("Введите координаты квадрата")
x = int(input("x = "))
y = int(input("y = "))
a = 20
penColor("red")
rectangle(x, y, x+a, y+a)

run()


