# Автор: Т.Е. Ганилова

a = set()
a.add(1)
b =[0] * 25
for i in range(8+1):
   c = set()
   # print(sorted(list(a))) #вывод всех получившихся чисел на очередном шаге
   for x in a:
       if 1000 <= x <= 1024:
           b[x % 1000] = 1
       c.add(x + 1)
       c.add(x + 5)
       c.add(x * 3)
   a = c
print(sum(b))