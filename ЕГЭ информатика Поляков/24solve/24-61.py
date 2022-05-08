# Автор: А.Н. Носкин

﻿with open( "k8-52.txt" ) as F:
  s = F.readline()

Max = 0 #макс длина цепочки одинаковых символов
k = 1 #длина текущей цепочки одинаковых символов 
c = s[0]   # символ, из которого строится самая длинная подцепочка 
for i in range(len(s)-1):
  if s[i] == s[i+1]:
    k += 1
    if k > Max:
      Max = k
      c = s[i] # запомнили новый символ
  else:
    k = 1 # появилась новая цепочка
print(c, Max)


