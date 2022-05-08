# Текстовый файл состоит из символов X, Y и Z.
# Определите максимальное количество идущих подряд пар
# символов ZX или ZY в прилагаемом файле.

s = open('24-196.txt').readline()
s = s.replace( 'Y', 'X' )
s = s.replace( 'ZX', '.' )
maxLen = curLen = 0
for c in s:
  if c == '.':
    curLen += 1
    maxLen = max( curLen, maxLen )
  else:
    curLen = 0
print( maxLen )

