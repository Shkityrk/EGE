target = '.'

with open("24-181.txt") as F:
  s = target + F.readline() + target

T = []
for i in range(len(s)):
  if s[i] == target:
    T.append( i )

ma = 0
for i in range(3,len(T)):
  ma = max(ma, T[i] - T[i-3] - 1)

print( target, ma )




