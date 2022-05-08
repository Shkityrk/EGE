s = open('24-181.txt').readline()

K = 7
stopPoints = [-1]*(K+1)
maxLen = 0
for i in range(len(s)):
  if s[i] == '.':
    stopPoints = [i]*(K+1)
  if s[i] in 'AEIOUY':
    stopPoints.insert( 0, i )
  maxLen = max( i - stopPoints[K], maxLen )

print( maxLen )

s = open('24-181.txt').readline()

K = 7
stopPoints = [-1]
maxLen = 0
for i in range(len(s)):
  if s[i] == '.':
    stopPoints = [i]
  if s[i] in 'AEIOUY':
    if len(stopPoints) > K:
      stopPoints.pop(0)
    stopPoints.append( i )
  maxLen = max( i - stopPoints[0], maxLen )

print( maxLen )