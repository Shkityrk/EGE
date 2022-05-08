s = open("24-181.txt").readline()

K = 7   # сколько гласных разрешается
stopPoints = [-1]*(K+1)
maxLen = 0
for i in range(len(s)):
  if s[i] == '.':
    stopPoints = [i]*(K+1)
  if s[i] in "AEIOUY":
    stopPoints.insert( 0, i )
  maxLen = max( i - stopPoints[K], maxLen )
print( maxLen )

"""
with open('24-181.txt') as f:
   s = f.readline()

parts = s.split('.')

maxLen, sMaxLen = 0, ''
for p in parts:
  lenP = len(p)
  for i in range(lenP):
    if lenP - i < maxLen: break
    j, countA = i, 0
    while j < lenP:
      if p[j] in 'AEIOUY':
        if countA == 7: break
        countA += 1
      j += 1
    if j - i > maxLen:
      maxLen = j - i
      sMaxLen = p[i:j]
    if j == lenP: break

print( maxLen, sMaxLen )
"""