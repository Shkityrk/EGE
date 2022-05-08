# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 16. Выбор максимального из двух
#

a = 4
b = 6

if a > b:
  M = a
else:
  M = b
print(M)

M = a
if b > a: M = b
print(M)

M = a if a > b else b
print(M)

M = max(a, b)
print(M)

