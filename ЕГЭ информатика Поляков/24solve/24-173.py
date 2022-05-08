with open("24-173.txt") as F:
  s = F.readline().strip()

Lmax = 5
L = 5
for i in range(len(s)-5):
  #print( s[i], state )
  if s[i:i+3] != s[i+3:i+6]:
    L += 1
    Lmax = max( L, Lmax )
  else:
    L = 5

print( Lmax )