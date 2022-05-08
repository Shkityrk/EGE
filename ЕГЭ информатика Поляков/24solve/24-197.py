# Текстовый файл состоит из символов X, Y и Z.
# Определите максимальное количество идущих подряд троек
# символов ZXY или ZYX в прилагаемом файле.

s = open('24-197.txt').readline()
s = s.replace( 'ZYY', '_' )
s = s.replace( 'ZXX', '_' )
s = s.replace( 'Y', 'X' )
s = s.replace( 'ZXX', '.' )
maxLen = curLen = 0
for c in s:
  if c == '.':
    curLen += 1
    maxLen = max( curLen, maxLen )
  else:
    curLen = 0
print( maxLen )

