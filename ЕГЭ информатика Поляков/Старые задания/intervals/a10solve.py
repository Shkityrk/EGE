# -*- coding: utf-8 -*-
"""
######################################################################
  Программа для решения задач типа А10, аналогичных демо-варианту
  ЕГЭ по информатике 2013 года
  (C) К.Ю. Поляков, 2012
  Web:    http://kpolyakov.narod.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
#-------------------------------------------------------
# Демо-вариант ФИПИ
#-------------------------------------------------------
# Неизвестная переменная - А, для остальных имен отрезков
# должны быть заданы начальные и конечные границы
# в форме кортежей.
#-------------------------------------------------------
intervals = {'P': (2,10), 'Q': (6,14) }
#-------------------------------------------------------
# Разрешенные операции:
#    ! - НЕ, отрицание
#    * - И, логическое умножение
#    + - ИЛИ, логическое сложение
#    -> или ^ - импликация
#    = - эквивалентность 
#-------------------------------------------------------
expr = '(A->P)+Q'

#-------------------------------------------------------
# Ещё примеры
#-------------------------------------------------------
# С операцией "не принадлежит"
#-------------------------------------------------------
#intervals = {'P': (2,20), 'Q': (15,25) }
#expr = '(!A->!P)+Q'
#-------------------------------------------------------
# Две импликации
#-------------------------------------------------------
#intervals = {'P': (0,40), 'Q': (20,45), 'R': (10,50) }
#expr = '(P->Q)+(!A->!R)'
#-------------------------------------------------------
# Выражение должно быть тождественно ложно
# (записываем в expr обратное)
#-------------------------------------------------------
#intervals = {'P': (10,25), 'Q': (15,30), 'R': (25, 40) }
#expr = '!(A*!P*(Q->!R))'
#-------------------------------------------------------
# Два выражения должны быть тождественно равны
# (записываем в expr их эквивалентность)
#-------------------------------------------------------
#intervals = {'P': (5,10), 'Q': (10,20), 'R': (25, 40) }
#expr = '(A->P)=(Q->R)'
#-------------------------------------------------------
# Два выражения должны быть различны для всех x
# (записываем в expr отрицание их эквивалентности)
#-------------------------------------------------------
#intervals = {'P': (10,15), 'Q': (5,20), 'R': (15, 25) }
#expr = '!((!A->P)=(Q->R))'

intervals = {'P': (10,40), 'Q': (5,15), 'R': (35, 50) }
expr = '(A->P)+(Q->R)'

intervals = {'P': (15,30), 'Q': (0,10), 'R': (25,35) }
expr = '(P->Q)+(A->R)'

intervals = {'P': (15,30), 'Q': (5,10), 'R': (10,20) }
expr = '(P->Q)*(!A)*R'

intervals = {'P': (8,39), 'Q': (23,58) }
expr = '(P*A)->(Q*A)'

#-------------------------------------------------------
#  TOTAL RANGE - определить полный интервал, захватываемый
#    заданными отрезками   
#-------------------------------------------------------
def TotalRange(intervals):
    first = True
    for (a,intv) in intervals.items():
        if first or intv[0] < xMin: xMin = intv[0]
        if first or intv[1] > xMax: xMax = intv[1]
        first = False
    return (xMin-1, xMax+1)    

#-------------------------------------------------------
#  AREA - класс, описывающий логическую функцию,
#    заданную отрезками с целочисленными границами
#-------------------------------------------------------
class area:
    def __init__(self, rangex, truthIntv = (0,0)):
        self.xMin = rangex[0]
        self.xMax = rangex[1]
        if type(truthIntv[0]) == str:
            self.vals = ['A']*(self.xMax - self.xMin)
        else:
            self.vals = [False]*(self.xMax - self.xMin)
            self.setRange(truthIntv, True)
    def setVal(self, x, val):
        self.vals[x-self.xMin] = val
    def getVal(self, x):
        return self.vals[x-self.xMin]
    def setRange(self, intv, val):
        for x in range(*intv):
            self.setVal(x, val)
    def getRange(self):
        return (self.xMin, self.xMax)
    def printVals(self):
        for x in range(self.xMin,self.xMax):
            y = self.getVal(x)
            if type(y) == str:
                print(str(x)+':', y)
            else:
                print(str(x)+':', int(y))
    def notOp(self):
        res = area((self.xMin,self.xMax))
        for x in range(*self.getRange()):
            if self.getVal(x) == 'A':
                res.setVal(x, '!A')
            elif self.getVal(x) == '!A':
                res.setVal(x, 'A')    
            else:
                res.setVal(x, not self.getVal(x))
        return res
    def orOp(self,other):
        res = area((self.xMin,self.xMax))
        for x in range(*self.getRange()):
            y1 = self.getVal(x)
            y2 = other.getVal(x)
            if type(y1) == bool:
                if type(y2) == bool:
                    y = y1 or y2
                else:
                    if y1: y = True
                    else:  y = y2
            elif type(y2) == bool:
                if y2: y = True
                else:  y = y1
            elif y1 == y2:
                  y = y1
            else: y = True                     
            res.setVal(x, y)
        return res
    def andOp(self,other):
        res = area((self.xMin,self.xMax))
        for x in range(*self.getRange()):
            y1 = self.getVal(x)
            y2 = other.getVal(x)
            if type(y1) == bool:
                if type(y2) == bool:
                    y = y1 and y2
                else:
                    if not y1: y = False
                    else:      y = y2
            elif type(y2) == bool:
                if not y2: y = False
                else:      y = y1
            elif y1 == y2:
                  y = y1
            else: y = False                     
            res.setVal(x, y)
        return res
    def __add__(self, other):
        return self.orOp(other)
    def __mul__(self, other):
        return self.andOp(other)
    def inv(self):
        return self.notOp()
    def imp(self, other):
        return self.notOp() + other
    def eqv(self, other):
        return self*other + self.notOp()*other.notOp()
    def __str__(self):
        (xMin, xMax) = self.getRange()        
        x = xMin
        xLeft = '-inf'
        value = self.getVal(x)
        s = ''
        while x < xMax:           
            while x < xMax and self.getVal(x) == value:
                x += 1
            if x >= xMax:
                  xRight = 'inf'
            else: xRight = x
            if s != '': s = s + "\n"
            s = s + '  ('+str(xLeft)+', '+str(xRight)+'): '
            if value == True: s = s + '1'
            elif value == False: s = s + '0'
            else: s = s + value
            if x < xMax:
                value = self.getVal(x)
                xLeft = x
                x += 1
        return s
                 
#-------------------------------------------------------
#  PRIORITY - определение приоритета логических операций
#-------------------------------------------------------
def priority(op):
    if   op == '=': return 1
    elif op == '^': return 2
    elif op == '+': return 3
    elif op == '*': return 4
    elif op == '!': return 5
    else: return 100
#-------------------------------------------------------
#  LAST PERFORMED OP - возвращает номер символа, который
#    содержит последнюю выполняемую операцию 
#-------------------------------------------------------
def lastPerformedOp(s):
    minPrt = 50
    lastOp = -1
    nest = 0
    for i in range(len(s)):
        if s[i] == '(':
            nest += 1
        elif s[i] == ')':
            nest -= 1
            if nest < 0:
                raise SyntaxError()
        elif nest == 0   and  priority(s[i]) <= minPrt:
            minPrt = priority(s[i])
            lastOp = i
    assert(nest==0)
    return lastOp
   
#-------------------------------------------------------
#  COMPUTE EXPR - вычисление логического выражения
#    с неизвестной переменной A
#-------------------------------------------------------
def computeExpr(s):
    if len(s) == 0: return 0
    k = lastPerformedOp(s)
    if k < 0:
        if s[0] == '('  and  s[-1] == ')':
            return computeExpr(s[1:-1])
        elif len(s) == 1:
            return vars[s]
        else: raise SyntaxError("Неверное логическое выражение '" + s + "'")
    else:
        res1 = computeExpr(s[0:k])
        res2 = computeExpr(s[k+1:])
        op = s[k]
        if   op == '*': res = res1 * res2
        elif op == '+': res = res1 + res2
        elif op == '!': res = res2.inv()
        elif op == '^': res = res1.imp(res2)
        elif op == '=': res = res1.eqv(res2)
        return res
#-------------------------------------------------------
#  SHOW INTERVALS - вывести на экран интервалы, где
#    функция имеет заданное значение
#-------------------------------------------------------
def showIntervals(R, value):
    (xMin, xMax) = R.getRange()
    x = xMin
    found = False
    while x < xMax:
      if R.getVal(x) == value:
        if x == xMin:
              xLeft = '-inf'
        else: xLeft = x
        while x < xMax and R.getVal(x) == value:
            x += 1
        if x >= xMax:
              xRight = 'inf'
        else: xRight = x
        print('    ('+str(xLeft)+', '+str(xRight)+')')
        found = True
      else:
        x += 1
    if not found:
        print('    нет')
#-------------------------------------------------------
# Основная программа
#-------------------------------------------------------
print("-------------------------------------------------------")
print("    Решение задачи А10 из демо-варианта ЕГЭ-2013       ")
print("-------------------------------------------------------")
print('Известные интервалы:')
for (k,v) in sorted(intervals.items()):
    print('    '+str(k)+': ' + str(v))
print('Выражение:', expr)
print("")
RangeX = TotalRange(intervals)
vars = {}
for (k,v) in intervals.items():
    vars[k] = area(RangeX, v)
vars['A'] = area(RangeX, ('A','A'))         

expr = expr.replace('->','^')
R = computeExpr(expr)
print('Где всегда 0 и A никак не может влиять:')
showIntervals(R, False)
print('Где всегда 1 и A может быть любым:')
showIntervals(R, True)
print('Где A обязательно истинно:')
showIntervals(R, 'A')
print('Где A обязательно ложно:')
showIntervals(R, '!A')

