"""
######################################################################
  Программа для решения задач 19-21 с одной кучей (2 + S + 2S)
  (C) К.Ю. Поляков, 2021
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
TARGET = 73
KADD, KADD2, KADD3 = 3, 13, 23
def gameOver( n1 ):
  return n1 >= TARGET

results = {}              # (1)
def gameResult( x ):
  if x in results: return results[x]     # (2)
  if gameOver(x): return 0
  nextCodes = [ gameResult( x+KADD ),
                gameResult( x+KADD2 ),
                gameResult( x+KADD3 )]
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  results[x] = res	# (3)
  return res

def hasMove( fromS, toResult ):
  total = 2 + S + 2*S;
  return toResult in \
         [gameResult(total+KADD), gameResult(total+KADD2),
          gameResult(total+KADD3)]

from math import ceil
ans1 = ceil( (TARGET-KADD3-KADD3-2)/3 )
ans2 = []
ans3 = []
for S in range(TARGET-1,0,-1):
  r = gameResult( 2+S+2*S )
  print( "%d: %d" % (S, r) )
  if r == 2: ans2.append(S)
  if r == -2 and hasMove(S, 1):
    ans3.append(S)

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", ans1)
print("2. ", sorted(ans2))
print("3. ", sorted(ans3))