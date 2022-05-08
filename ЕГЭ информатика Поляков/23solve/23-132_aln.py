# 23.132
# Автор решения: А.Л. Наймушин
'''
У исполнителя есть три команды, которым присвоены номера: 
1. Прибавить 1
2. Добавить справа 0
3. Добавить справа 1
Первая команда увеличивает число на 1. При выполнении второй команды,
исполнитель приписывает справа к числу 0, а при выполнении третьей команды
приписывает справа к числу 1. (например, для числа 10 результатом работы
данных команд будут являться числа 100 и 101 соответственно). 
Сколько существует программ, которые исходное двоичное число 101
преобразуют в двоичное число 101110?
'''

def f( a, b ):
  if a == b: return 1
  if a > b: return 0
  return f( a+1, b ) +  f( int(f"{a:b}"+'0', 2), b)+\
         + f( int(f"{a:b}"+'1', 2), b)
def g( a, b ):
  if a == b: return 1
  if int(a,2) > int(b,2): return 0
  return g( bin(int(a,2)+1)[2:], b ) + g( a+'0', b ) + g( a+'1', b )

print( f( 5, 46 ) )
print( g( '101', '101110' ) )

#Rez = 254

