# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 29. Циклы в графике
#

from graph import *

for x in range(20,101,20):
  circle(x, 20, 5)

for y in range(120,161,20):
  for x in range(20,101,20):
    circle(x, y, 5)


def Row(y):
  for x in range(20,101,20):
    circle(x, y, 5)

for y in range(220,261,20):
  Row(y)

run()
