# 23.127
# Автор решения: А.Л. Наймушин
'''
У исполнителя есть две команды, которым присвоены номера:
1. Умножить на 2
2. Умножить на 3
Первая команда увеличивает число на экране в 2 раза,
вторая – увеличивает значение в 3 раза.
Сколько существует программ, для которых при исходном числе 8
результатом является число 3456, и при этом траектория вычислений
содержит число 96.
'''




# Функция подсчета количества цепочек команд (программ).
# x - текущее число, t - цель (target).
def nProg( x, t ): 
    if x == t:   # если цель достигнута, то
        return 1 # завершить функцию, посчитав цепочку (программу)
    if x > t:    # если перелет, то
        return 0 # завершить функцию, не считая цепочку 
    # x < t - продолжаем строить дерево:
    return nProg( x*2, t ) + nProg( x*3, t )
print( nProg( 8, 96 ) * nProg( 96, 3456 ) )
