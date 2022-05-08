# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 1 (8 класс)
# Программа № 4. Сумма целых чисел
#

print( 12345 + 67890 )

num1 = 12345
num2 = 67890
print( num1 + num2 )

num1 = input( "n1 = " )
num2 = input( "n2 = " )
summa = num1 + num2
print( summa )

print( "Введите два целых числа:" )
num1 = int(input())
num2 = int(input())
summa = num1 + num2
print(num1, "+", num2, "=", summa, sep = "")

print( "Введите два целых числа:" )
num1, num2 = map(int, input().split())
summa = num1 + num2
print(num1, "+", num2, "=", summa, sep = "")

