# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 15. Случайные числа
#

from random import randint
n = randint(1, 6)
print(n)
n = randint(1, 6)
print(n)
n = randint(1, 6)
print(n)

from random import uniform
x = uniform(5, 12)
print(x)
x = uniform(5, 12)
print(x)
x = uniform(5, 12)
print(x)