# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 21. Сложные условия
#

age = 34
if age >= 25 and age <= 40:
  print("подходит")
else:
  print("не подходит")

if 25 <= age <= 40:
  print("подходит")
else:
  print("не подходит")

if age < 25 or age > 40:
  print("не подходит")
else:
  print("подходит")

a = 123
if 100 <= a and a < 1000 and a % 7 == 0:
  print("Да!")
else:
  print("Нет.")

digits3 = (100 <= a and a < 1000)
div7 = (a % 7 == 0)
if digits3 and div7:
  print("Да!")
else:
  print("Нет.")

day = 3
if day == 1 or day == 4:
  print("Полетит!")
else:
  print("Нет рейса.")

fly = (day == 1 or day == 4)
if fly:
  print("Полетит!")
else:
  print("Нет рейса.")

if not(day == 1 or day == 4):
  print("Нет рейса.")
else:
  print("Полетит!")
