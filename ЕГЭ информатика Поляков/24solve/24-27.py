# Автор: А.Н. Носкин

# два способа решения:
# - добавлением полного блока букв или по буквенно
with open("k7b-1.txt") as Fin:
  s = Fin.readline()

"""
Постоянно повторяется фрагмент EAB,
поэтому возможны 3 варианта окончания строки:
1 тип = ..EABE - неполный последний фрагмент
2 тип = ..EABEB - неполный последний фрагмент
3 тип = ..EAB - полный последний фрагмент
"""

# 1й способ решения:
c = 'EAB'
while c in s: # ищем EAB, потом EABEAB и т.д
    c += 'EAB'

if c[:-1] in s: #2 тип
  print(len(c)-1)
elif c[:-2] in s: #1 тип
  print(len(c)-2)
else:
    print(len(c)-3) #3 тип 
# минус 1, 2 или 3, чтобы убрать лишнии буквы

# 2й способ
with open("k7b-1.txt") as Fin:
  s = Fin.readline()

c = 'EAB'
while c in s: # ищем EAB, потом EABE и т.д
    if c[-1]=="B": c +="E"
    elif c[-1]=="A": c +="B"
    elif c[-1]=="E": c +="A"
print(len(c)-1) 


