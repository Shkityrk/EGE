# Автор: А. Наймушин
# задача 14.221

x = 2**5*3**25
print (x)
count0 = 0
count1 = 0
count2 = 0
s = ''
while x:
    s += str(x % 3)
    #print (s)
    if x % 3 == 0:
      count0 += 1
    if x % 3 == 1:
      count1 += 1
    if x % 3 == 2:
      count2 += 1
      #print (x)
    x //= 3
print( 'Ответ:','0 = ', count0,'  1 = ',count1,'  2 = ',count2 )

# Ответ:
"""
Выражение (2**5)*(3**25) записано в троичной системе
счисления. Определите,  сколько в этой записи цифр 0, 1 и 2.
"""
