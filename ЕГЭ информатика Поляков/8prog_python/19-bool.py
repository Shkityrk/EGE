# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 19. Логические переменные
#

b = True
b = False
print(type(b))

a = 4
b = 5
c = 4
found = False   # пока не нашли пару равных
if a == b: found = True  # проверяем пару a-b
if a == c: found = True  # проверяем пару a-c
if b == c: found = True  # проверяем пару b-c
if found:
  print("Нашли равные!")
else:
  print("Равных нет.");

found = (a == b)
if a == c: found = True  # проверяем пару a-c
if b == c: found = True  # проверяем пару b-c
if found:
  print("Нашли равные!")
else:
  print("Равных нет.");
