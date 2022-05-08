# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 14. Вещественные числа
#

x = 4.0
print(type(x))

qElectron = 1.60217662e-19
print(qElectron)

distToSun = 1.496e11
print(distToSun)

x = 0.1
y = 0.2
print(x + y)
diff = x + y - 0.3
print(diff)

x = float(input("Введите число"))
print(type(x))

print("Введите три числа")
x, y, z = map(float, input().split())
print(x, y, z)

x = 16 / 7
print(x)
print(">{:f}".format(x))	 # >2.285714
print(">{:10.3f}".format(x))	 # >     2.286
print(">{:.3f}".format(x))	 # >2.286
x = 1e10/7
print(">{:12.4e}".format(x)) # >  1.4286e+09

import math
x = math.sqrt(5)
print('sqrt(5) =', x)

from math import sqrt, pi
x = sqrt(5)
print('sqrt(5) =', x)
R = 12
circleLen = 2*pi*R
print('L =', circleLen)
