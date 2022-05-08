from string import ascii_uppercase

countAll = 0
maxLen = 0
with open('24-174.txt') as F:
  while True:
    s = F.readline().strip()
    if not s: break
    if s.count('R') >= 30: continue
    for letter in ascii_uppercase:
      indices = []
      for i, c in enumerate(s):
        if c == letter:
          indices.append( i )
      if len(indices) > 1:
        #print( letter, indices )
        diffs = []
        for i in range(len(indices)-1):
          diffs.append( indices[i+1]-indices[i] )
          if diffs[-1] > 1:
            countAll += 1
        if diffs:
          maxLen = max( maxLen, max(diffs) )

print( maxLen, countAll )