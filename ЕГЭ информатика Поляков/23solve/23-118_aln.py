# 23.118
# Автор решения: А.Л. Наймушин
'''
У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 2
3. Умножить на 2
Сколько разных чисел на отрезке [34, 59] может быть получено из числа 1
с помощью программ, состоящих из 6 команд?
'''
Ncmd = 6

def rec( n, remains, target, way ):
  way += [n]
  if remains == 0:
    if n == target:
      #print( way )
      return 1
    return 0
  return rec( n+1, remains-1, target, way[:] ) + \
         rec( n+2, remains-1, target, way[:] ) + \
         rec( n*2, remains-1, target, way[:] )

count = 0
for target in range(34, 59+1):
  if rec(1, Ncmd, target, [] ) > 0:
    count += 1

print( count )

#Rez = 11

