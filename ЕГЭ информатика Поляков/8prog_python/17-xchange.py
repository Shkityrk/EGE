# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 17. Обмен значениями переменных
#

a = 6
b = 4

print(a, b)
if a > b:
  temp = a
  a = b
  b = temp
print(a, b)

a = 7
b = 5
print(a, b)
if a > b:
  a, b = b, a
print(a, b)

