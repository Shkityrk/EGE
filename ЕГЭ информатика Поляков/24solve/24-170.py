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
    if L > Lmax:
       print(L)
       print(s[i-Lmax:i+1])
    Lmax = max( L, Lmax )
    state = (state + 1) % 3
  else:
    L = 1
    state = target.index(s[i])
    state = (state + 1) % 3
  #print( L, Lmax, state )

print( Lmax )