# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 6. Рисование линий
#

from graph import *

penColor("blue")

point(10, 20)
point(11, 20)
point(12, 20)
point(13, 20)
point(14, 20)
point(15, 20)

point(10, 20)
point(11, 21)
point(12, 22)
point(13, 23)
point(14, 24)
point(15, 25)

penColor(255, 0, 0)
line(100, 100, 150, 220)

penSize(5)
line(100, 220, 150, 100)

run()


