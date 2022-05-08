with open("24-169.txt") as F:
  s = F.readline().strip()

#s = 'ZZZXYZXYZXZZZXYZX'
target = 'XYZ'

Lmax = 0
L = 0
state = 0 # 'X'
for i in range(len(s)):
  #print( s[i], state )
  if s[i] == target[state]:
    L += 1
    state = (state + 1) % 3
    if state == 0:
      Lmax = max( L, Lmax )
  else:
    L = 0
    state = 0
  #print( L, Lmax, state )

print( Lmax )