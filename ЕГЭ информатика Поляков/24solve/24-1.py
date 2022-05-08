# Автор: А.Н. Носкин

# 1-й способ
with open("k7-0.txt") as F:
  s = F.readline() # считали строку

Max = 0 # макс длина цепочки из "С"
Len_C = 0 # начальная длина цепочки из "С"
for c in s:
  if c == 'C':
    Len_C += 1   # появилась еще буква "С"
    if Len_C > Max: # перезаписали длину
       Max = Len_C
  else:
    Len_C = 0 # при другой букве сбрасываем счетчик
print(Max)

""" 2-й способ идея Б.С. Михлина"""

with open("k7-0.txt") as Fin:
  s = Fin.readline()

c = 'C'
while c in s: # ищем CC, потом CCC и т.д
  c += 'C'
print(len(c)-1 )
# минус 1, чтобы убрать лишнюю (последнюю добавленную С)





