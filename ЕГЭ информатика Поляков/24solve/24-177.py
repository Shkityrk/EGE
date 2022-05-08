with open('24-157.txt') as F:
  s = F.readline()

#s = 'RPASPRLKJRPQWERPR'

maxLen = 0
curLen = 0
prev = '*'
for c in s:
  if (prev == 'P' and c == 'R') or \
     (prev == 'R' and c == 'P'):
    curLen = 1
  else:
    curLen += 1
    maxLen = max( maxLen, curLen )
  #print(prev, c, curLen)
  prev = c

print( maxLen )
