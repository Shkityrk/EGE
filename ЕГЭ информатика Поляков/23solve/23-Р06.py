TARGET = 4
def nProg( x ):
    if x == TARGET: # если цель достигнута, то
        return 1    # завершить функцию, посчитав цепочку (программу)
    if x < TARGET:  # если перелет, то
        return 0 # завершить функцию, не считая цепочку
    # x > TARGET - продолжаем строить дерево:
    n = nProg( x - 1 )
    if x % 2 == 0:
      n += nProg( x // 2 )
    return n

START = 24
print( nProg( START//2-1 ) + nProg( START-1-1 ) )
