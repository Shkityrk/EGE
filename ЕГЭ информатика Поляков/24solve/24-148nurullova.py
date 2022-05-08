﻿# Автор А. Нуруллова

"""
148)	Текстовый файл 24-s2.txt содержит только заглавные буквы
латинского алфавита (ABC…Z). Определите символ, который чаще всего
встречается в файле сразу после буквы X. В ответе запишите сначала этот символ,
а потом сразу (без разделителя) сколько раз он встретился после буквы X. Если таких
символов несколько, нужно вывести тот, который стоит раньше в алфавите.
Например, в тексте XBCXXBXDDD после буквы
X два раза стоит B, по одному разу – X и D. Для этого текста ответом будет B2.
"""

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = [0]*26
with open("24-s2.txt") as F:
  s = F.readline() # считали строку
for i in range(len(s)-1):
  if s[i] == "X":
    pos = ABC.find( s[i+1] )
    count[pos] += 1
mx = max(count)
no = count.index(mx)
print( ABC[no], mx )
