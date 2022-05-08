# 23.126
# Автор решения: А.Л. Наймушин
'''
У исполнителя есть две команды, которым присвоены номера:
1. Прибавить 3
2.Умножить на 2
Первая команда увеличивает число на экране на 3,
вторая – увеличивает значение в два раза.
Сколько существует программ, для которых при исходном числе 12
результатом является число 96?

Rez = 40
'''

# Функция подсчета количества цепочек команд (программ).
# x - текущее число, t - цель (target).
def nProg( x, t ): 
    if x == t:   # если цель достигнута, то
        return 1 # завершить функцию, посчитав цепочку (программу)
    if x > t:    # если перелет, то
        return 0 # завершить функцию, не считая цепочку 
    # x < t - продолжаем строить дерево:
    return nProg( x+3, t ) + nProg( x*2, t )
print( nProg( 12, 96 )  )
