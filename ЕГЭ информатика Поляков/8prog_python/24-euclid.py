# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 24. Алгоритм Евклида
#

a = 14
b = 21
count = 0
while a != 0 and b != 0:
  if a > b:
    a = a % b
  else:
    b = b % a
  count += 1

if a != 0:
  print(a)
else:
  print(b)

print(a+b)
