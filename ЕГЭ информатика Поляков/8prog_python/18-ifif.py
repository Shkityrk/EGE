# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 18. Вложенные условные операторы
#

ageA = 15
ageB = 17
if ageA > ageB:
  print("Андрей старше")
else:
  if ageA == ageB:
    print("Одного возраста")
  else:
    print("Борис старше")

if ageA > ageB:
  print("Андрей старше")
elif ageA == ageB:
  print("Одного возраста")
else:
  print("Борис старше")

cost = 1500
if cost < 1000:
  print("Скидок нет.")
elif cost < 2000:
  print("Скидка 2%.")
elif cost < 5000:
  print("Скидка 5%.")
else:
  print("Скидка 10%.")
