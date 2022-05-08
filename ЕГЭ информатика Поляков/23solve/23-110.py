START = 3
TARGET = 22
MID = 10
NO =  [8, 15]

def nProg( x, target ):
  if x in NO:     # запретные значения
    return False
  if x == target: # если цель достигнута, то
    return 1    # завершить функцию, посчитав цепочку (программу)
  if x > target:  # если перелет, то
      return 0 # завершить функцию, не считая цепочку
  # x < target - продолжаем строить дерево:
  return nProg(x+1, target) + nProg(x+2, target) + nProg(x*3, target)

print( nProg(START, MID) * nProg(MID, TARGET) )
