with open("24-175.txt") as f:
  s = f.readline()

allLen = [ len(chunk) for chunk in s.split("KEGE") ]
N = len(allLen)
maxLen = 0
for i in range(N-2):
  L = sum( allLen[i:i+3] ) + 4*len("KEGE") - 2
  if i == 0 and allLen[i] != 0:
    L -= len("KEGE") - 1
  if i+2 == N-1 and allLen[-1] != 0:
    L -= len("KEGE") - 1
  maxLen = max( L, maxLen )

print( maxLen )


stopPoints = [0, 0, 0]
maxLen = 0
for i in range(3,len(s)):
  if s[i-3:i+1] == "KEGE":
    stopPoints.append(i-2)
  maxLen = max( i - stopPoints[-3] + 1, maxLen )

print( maxLen )
