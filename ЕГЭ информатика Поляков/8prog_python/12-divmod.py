# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 12. Остаток от деления
#

timeSec = 289
minutes = timeSec // 60   # = 4
seconds = timeSec % 60    # = 49

print( timeSec, "с =", minutes, "мин", seconds, "сек")

N = 123
print(N, "=")
lastDigit = N % 10   # = 3
digits2 = N // 10
print(digits2, "*10 +", lastDigit)

print (7 // 2, 7 % 2)
print (-7 // 2, -7 % 2)
