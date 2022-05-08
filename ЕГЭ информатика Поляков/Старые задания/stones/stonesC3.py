"""
######################################################################
  Программа для решения задач типа С3, аналогичных демо-варианту
  ЕГЭ по информатике 2013 года
  (C) К.Ю. Поляков, 2012
  Web:    http://kpolyakov.narod.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
#-----------------------------------------------------------------
# Демо-вариант ФИПИ
# Вариант с двумя возможными ходами
#-----------------------------------------------------------------

MAX_STONES = 22
def Oper1(n): return n+1
def Oper2(n): return n*2
operations = [Oper1, Oper2]

#-----------------------------------------------------------------
# Другой вариант с тремя возможными ходами
#-----------------------------------------------------------------
"""
MAX_STONES = 75
def Oper1(n): return n+3
def Oper2(n): return n*4
operations = [Oper1, Oper2]
"""
#-----------------------------------------------------------------
# Вариант с тремя возможными ходами
#-----------------------------------------------------------------
"""
MAX_STONES = 30
def Oper1(n): return n+2
def Oper2(n): return n+3
def Oper3(n): return 2*n
operations = [Oper1, Oper2, Oper3]
"""

MAX_STONES = 32
def Oper1(n): return n+1
def Oper2(n): return 3*n+1
operations = [Oper1, Oper2]

MAX_STONES = 48
def Oper1(n): return n+1
def Oper2(n): return n+3
def Oper3(n): return 3*n
operations = [Oper1, Oper2, Oper3]

print("-------------------------------------------------------")
print("    Решение задачи C3 из демо-варианта ЕГЭ-2013       ")
print("-------------------------------------------------------")
print('Число камней для окончания игры:', MAX_STONES)

#-------------------------------------------------------
# GAME OVER - условие окончания игры
#-------------------------------------------------------
def GameOver(n):
    global MAX_STONES
    return n >= MAX_STONES

#-------------------------------------------------------
# EVALUATE POSITION - определение типа позиции
#   (выигрышная или проигрышная) и числа ходов до
#   окончания игры
#-------------------------------------------------------
def EvaluatePosition(n, operations):
    winSteps = -1
    lossSteps = -1
    for op in operations:
        if GameOver(op(n)): return ("W", 1)    
    for op in operations:
        nextVal = op(n)
        (result,steps) = positionTable[nextVal]
        if result == "W":
            if steps > lossSteps: lossSteps = steps
        else:
            steps += 1
            if winSteps < 0  or steps < winSteps:
                winSteps = steps                
    if winSteps >= 0:
          return ("W", winSteps)
    else: return ("x", lossSteps)

#-------------------------------------------------------
# Заполнение таблицы, указывающей выигрышные и
# проигрышные позиции
#-------------------------------------------------------
ans1a = []
ans1b = []
ans2 = []
ans3 = []
positionTable = {}
for i in range(MAX_STONES-1,0,-1):
    positionTable[i] = EvaluatePosition(i, operations)
    r, steps = positionTable[i]
    if r == "W":
        print("%2d: выигрыш (%d) " % (i, steps))
        if steps == 1: ans1a.insert(0,i)
        if steps == 2: ans2.insert(0,i)
    else:
        print("%2d: :-( (%d)" % (i, steps))
        if steps == 1: ans1b.insert(0,i)
        if steps == 2: 
            for op in operations:
                nextVal = op(i)
                (result,steps) = positionTable[nextVal]
                if steps == 1:
                    if not i in ans3:
                        ans3.insert(0,i)
#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print(" Вопрос 1а: " + str(ans1a))
print(" Вопрос 1б: " + str(ans1b))
print(" Вопрос 2:  " + str(ans2))
print(" Вопрос 3:  " + str(ans3))

