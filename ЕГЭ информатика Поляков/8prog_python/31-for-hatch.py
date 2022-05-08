# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 31. Штриховка
#

from graph import *

x1 = 100; x2 = 300
y1 = 100; y2 = 200
rectangle(x1, y1, x2, y2)

N = 16
h = round((x2-x1)/N)          # шаг штриховки - целый
for x in range(x1+h, x2, h):
  line(x, y1, x, y2)


y1 += 200
y2 += 200
rectangle(x1, y1, x2, y2)

h = (x2-x1) / N               # шаг штриховки - вещественный
x = x1 + h
while x < x2:
  line(round(x), y1, round(x), y2)
  x += h

run()
