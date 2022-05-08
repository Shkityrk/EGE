with open('24-157.txt') as F:
  s = F.readline()

STOP = 'QW'
#s = 'QWABCQWQWBNMPQWRTY'
chunks = [ c for c in s.split(STOP) if c]

maxLen = 0
for i, ch in enumerate(chunks):
  curLen = len(ch) + 2
  if (i == 0 and not s.startswith(STOP) or
      i == len(chunks)-1 and not s.endswith(STOP)) :
    curLen -= 1
  #print( curLen )
  maxLen = max( maxLen, curLen )

print( maxLen )
