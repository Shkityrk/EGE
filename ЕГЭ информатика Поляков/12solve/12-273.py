# 12.273
# Автор: А.Л. Наймушин

s =   '32'*15 +'42'*5 +'4'*5
while '42' in s or '32' in s:
  if '42' in s:
    s = s.replace('42', '51', 1)
  else:
    s = s.replace('32', '61', 1)
print('Конечная строка = ',s)
Sum_c = sum(map(lambda x:int(x) if x.isdigit() else 0,s))
print('Максимальная сумма цифр в конечной строке =', Sum_c )

'''
616161616161616161616161616161515151515144444
155
'''
