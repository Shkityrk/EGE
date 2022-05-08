# Автор: А.Н. Носкин

"""
Идея: в массив записываем цепочки длиной
равные или больше чем предыдущие.
Последний элемент массива (цепочка) будет самой
большой длины. При выводе печатаем первый символ цепочки
максимальной длины.
"""
with open("k8-4.txt") as F:
  s = F.readline() # считали строку

a=[] # массив хранения цепочек
stroka = s[0]
Max = 1
for i in range(len(s)-1):
  if s[i] == s[i+1]: # собираем цепочку из одинаковых символов
    stroka += s[i+1]
  else:
    if len(stroka)>= Max:
      Max = len(stroka)
      a.append(stroka) #Цепочка прервалась, записываем в массив
    stroka = s[i+1] # появилась новая буква 

if s[-1]==s[-2]: # проверка последней цепочки
  if len(stroka)>= Max:
      Max = len(stroka)
      a.append(stroka)
  
for x in a: # для всех символов в массиве
  if len(x)== Max:
    print( x[0], Max ) # вывести символ и длину




 




