# 23.130
# Автор решения: А.Л. Наймушин
'''
У исполнителя есть три команды, которым присвоены номера:
1.  Прибавить 2
2. Прибавить 3
3. Умножить на 2
Первая команда увеличивает число на 2, вторая – на 3,
третья – увеличивает число вдвое. Сколько различных чисел может быть получено
из числа 10 всеми возможными алгоритмами длиной 5 команд? 
'''

Ncmd = 5

def rec( n, remains, target, way ):
  way += [n]
  if remains == 0:
    if n == target:
      #print( way )
      return 1
    return 0
  return rec( n+2, remains-1, target, way[:] ) + \
         rec( n+3, remains-1, target, way[:] ) + \
         rec( n*2, remains-1, target, way[:] )

count = 0
for target in range(1, 1000+1):
  if rec(10, Ncmd, target, [] ) > 0:
    count += 1

print( count )

#Rez = 83


