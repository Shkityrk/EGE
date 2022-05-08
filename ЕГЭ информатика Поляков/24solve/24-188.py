with open('24-181.txt') as f:
   s = f.readline()

parts = s.split('Y')

maxLen, sMaxLen = 0, ''
for p in parts:
  lenP = len(p)
  for i in range(lenP):
    if lenP - i < maxLen: break
    j, countPoints = i, 0
    while j < lenP:
      if p[j] == '.':
        if countPoints == 5: break
        countPoints += 1
      j += 1
    if j - i > maxLen:
      maxLen = j - i
      sMaxLen = p[i:j]
    if j == lenP: break

print( maxLen, sMaxLen )

