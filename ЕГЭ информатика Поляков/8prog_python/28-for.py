# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 28. Цикл по переменной
#

for i in range(10):
  print("Привет!")

for i in [0,1,2,3,4,5,6,7,8,9]:
  print("Пока!")

N = 2
for power in range(1,11):
  print(N)
  N *= 2

summa = 0
for i in range(1,1001):
  summa += i
print(summa)

for k in range(10,0,-1):
  print(k*k)

for i in range(0, 101, 5):
  print(i)
